from pathlib import Path
from typing import Generator

try:
    from ..utils.config import Colors
except ImportError:
    class Colors:
        GREEN = '\033[32m'
        RESET = '\033[39m'
        HEADER = '\033[95m'


def search_files(directory: Path, extension: str) -> Generator[Path, None, None]:
    """
    Searches for files with a specific extension in a directory recursively.
    
    Args:
        directory (Path): Directory to search in.
        extension (str): File extension to look for (e.g. '.py' or 'py').
        
    Yields:
        Path: Path object of found file.
    """
    directory = Path(directory)
    if not directory.exists():
        print(f"Directory not found: {directory}")
        return

    # Normalize extension
    if not extension.startswith("."):
        extension = f".{extension}"
    header_msg = f"{Colors.HEADER}Searching for *{extension} in {directory}...{Colors.RESET}"
    print(header_msg)

    for path in directory.rglob(f"*{extension}"):
        yield path


if __name__ == "__main__":
    try:
        target_dir = input("Directory to search: ")
        ext = input("Extension (e.g. txt): ")
        
        if target_dir and ext:
            found_count = 0
            for file_path in search_files(Path(target_dir), ext):
                print(f"{Colors.GREEN}[+] {file_path}{Colors.RESET}")
                found_count += 1
            
            print(f"\n{Colors.HEADER}Total found: {found_count}{Colors.RESET}")
        else:
            print("Invalid input.")
            
    except KeyboardInterrupt:
        print("\nAborted.")
