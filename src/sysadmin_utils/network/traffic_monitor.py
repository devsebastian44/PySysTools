import os
import time
import psutil
import pandas as pd


UPDATE_DELAY = 1  # Seconds


def get_size(bytes_val: int) -> str:
    """
    Converts bytes to a human-readable format (KB, MB, GB, etc.).
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes_val < 1024:
            return f"{bytes_val:.2f}{unit}B"
        bytes_val /= 1024
    return f"{bytes_val:.2f}PB"


def clear_screen():
    """Clears the console screen."""
    import subprocess
    subprocess.run(["cls"] if os.name == "nt" else ["clear"], shell=False)


def monitor_traffic(delay: float = 1.0):
    """
    Monitors network traffic and prints statistics to the console.
    """
    io = psutil.net_io_counters(pernic=True)

    try:
        while True:
            time.sleep(delay)
            io_2 = psutil.net_io_counters(pernic=True)
            data = []

            for iface, iface_io in io.items():
                if iface not in io_2:
                    continue

                upload_speed = io_2[iface].bytes_sent - iface_io.bytes_sent
                download_speed = io_2[iface].bytes_recv - iface_io.bytes_recv

                data.append({
                    "Interface": iface,
                    "Download Total": get_size(io_2[iface].bytes_recv),
                    "Upload Total": get_size(io_2[iface].bytes_sent),
                    "Upload Speed": f"{get_size(upload_speed / delay)}/s",
                    "Download Speed": f"{get_size(download_speed / delay)}/s",
                    "Raw Download": download_speed  # For sorting
                })

            io = io_2
            df = pd.DataFrame(data)

            if not df.empty:
                df.sort_values("Raw Download", inplace=True, ascending=False)
                df.drop(columns=["Raw Download"], inplace=True)

                clear_screen()
                print(df.to_string(index=False))

    except KeyboardInterrupt:
        print("\nStopping monitor...")


if __name__ == "__main__":
    print("Starting Network Traffic Monitor... (Ctrl+C to stop)")
    monitor_traffic(UPDATE_DELAY)
