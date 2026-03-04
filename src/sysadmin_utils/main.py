import argparse
import sys
from pathlib import Path

# Add src to python path to allow running this script directly if needed
sys.path.append(str(Path(__file__).parent.parent.parent))

# flake8: noqa: E402
from src.sysadmin_utils.utils.config import APP_NAME, VERSION, Colors
from src.sysadmin_utils.security import password_manager, malware_scanner, hash_utils
from src.sysadmin_utils.network import traffic_monitor, connectivity, active_connections, \
    downloader, samba_enum
from src.sysadmin_utils.network.ftp import FTPClient
from src.sysadmin_utils.system import formatting
from src.sysadmin_utils.data import file_search
from src.sysadmin_utils.ui import screenshot


def main():
    parser = argparse.ArgumentParser(
        description=f"{APP_NAME} - System Administration Utilities")
    parser.add_argument("--version", action="version", version=f"{APP_NAME} {VERSION}")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Password Generator
    pwd_parser = subparsers.add_parser(
        "gen-pass", help="Generate a secure password")
    pwd_parser.add_argument(
        "-l", "--length", type=int, default=16, help="Password length")
    pwd_parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")

    # Malware Scanner
    scan_parser = subparsers.add_parser(
        "scan-malware", help="Scan a directory for malware")
    scan_parser.add_argument("path", help="Path to scan")

    # Hash Check
    hash_parser = subparsers.add_parser("hash-check", help="Calculate or check file hash")
    hash_parser.add_argument("path", help="File to check")

    # Network Tools
    net_parser = subparsers.add_parser("net-monitor", help="Monitor network traffic")
    net_parser.add_argument("-d", "--delay", type=float, default=1.0, help="Update delay")

    subparsers.add_parser("check-internet", help="Check internet connectivity")
    subparsers.add_parser("list-connections", help="List active network connections")

    dl_parser = subparsers.add_parser("download", help="Download a file from URL")
    dl_parser.add_argument("url", help="URL to download")
    dl_parser.add_argument("path", help="Destination path")

    samba_parser = subparsers.add_parser("samba-enum", help="Enumerate Samba shares")
    samba_parser.add_argument("target", help="Target IP")

    # File Tools
    org_parser = subparsers.add_parser("organize", help="Organize files by extension")
    org_parser.add_argument("path", help="Directory to organize")
    org_parser.add_argument("-w", "--watch", action="store_true", help="Watch directory")

    search_parser = subparsers.add_parser("search", help="Search for files")
    search_parser.add_argument("path", help="Directory to search")
    search_parser.add_argument("extension", help="File extension")

    # UI Tools
    screen_parser = subparsers.add_parser("screenshot", help="Take a screenshot")
    screen_parser.add_argument("output", help="Output file path")

    ftp_parser = subparsers.add_parser("ftp", help="FTP Client Operations")
    ftp_parser.add_argument("action", choices=["list", "upload", "download"], help="Action to perform")
    ftp_parser.add_argument("--host", required=True, help="FTP Host")
    ftp_parser.add_argument("--user", required=True, help="FTP User")
    ftp_parser.add_argument("--password", required=True, help="FTP Password")
    ftp_parser.add_argument("--local", help="Local file path")
    ftp_parser.add_argument("--remote", help="Remote file path")

    args = parser.parse_args()

    if args.command == "gen-pass":
        pwd = password_manager.generate_password(args.length, not args.no_symbols)
        print(f"Generated Password: {Colors.GREEN}{pwd}{Colors.RESET}")

    elif args.command == "scan-malware":
        malware_scanner.scan_directory(args.path)

    elif args.command == "hash-check":
        h = hash_utils.calculate_file_hash(Path(args.path))
        print(f"SHA-256: {h}")

    elif args.command == "net-monitor":
        print(f"{Colors.HEADER}Starting Network Monitor...{Colors.RESET}")
        traffic_monitor.monitor_traffic(args.delay)

    elif args.command == "check-internet":
        print("Checking connectivity...")
        if hasattr(connectivity, 'test_internet_connection'):
            connectivity.test_internet_connection()
        else:
            print("Connectivity module not fully compatible.")

    elif args.command == "list-connections":
        conns = active_connections.get_remote_connections()
        for c in conns:
            print(f"{c['Process Name']} ({c['Process ID']}) -> {c['Remote Address']}")

    elif args.command == "download":
        downloader.download_file(args.url, args.path)

    elif args.command == "samba-enum":
        samba_enum.enumerate_shares(args.target)

    elif args.command == "organize":
        if args.watch:
            formatting.watch_directory(args.path)
        else:
            formatting.organize_directory(args.path, verbose=True)

    elif args.command == "search":
        count = 0
        for f in file_search.search_files(args.path, args.extension):
            print(f"[+] {f}")
            count += 1
        print(f"Found {count} files.")

    elif args.command == "screenshot":
        screenshot.take_screenshot(args.output)

    elif args.command == "ftp":
        client = FTPClient(args.host, args.user, args.password)
        try:
            client.connect()
            if args.action == "list":
                files = client.list_files()
                for f in files:
                    print(f"- {f}")
            elif args.action == "upload":
                if not args.local:
                    print("Error: --local path required for upload")
                else:
                    client.upload_file(args.local, args.remote)
            elif args.action == "download":
                if not args.remote:
                    print("Error: --remote filename required for download")
                else:
                    client.download_file(args.remote, args.local)
            client.close()
        except Exception as e:
            print(f"FTP Error: {e}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
