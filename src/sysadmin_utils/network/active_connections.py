import psutil


def get_remote_connections():
    """Obtains active remote connections."""
    remote_connections = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == psutil.CONN_ESTABLISHED:
            local_address, local_port = conn.laddr
            remote_address, remote_port = conn.raddr
            process = psutil.Process(conn.pid)
            remote_connections.append({
                'Local Address': f"{local_address}:{local_port}",
                'Remote Address': f"{remote_address}:{remote_port}",
                'Process Name': process.name(),
                'Process ID': conn.pid,
            })
    return remote_connections


def main():
    """Script entry point."""
    remote_connections = get_remote_connections()
    if remote_connections:
        for conn in remote_connections:
            print("Local Address:", conn['Local Address'])
            print("Remote Address:", conn['Remote Address'])
            print("Process Name:", conn['Process Name'])
            print("Process ID:", conn['Process ID'])
            print("-" * 40)
    else:
        print("No remote connections found.")


if __name__ == "__main__":
    main()
