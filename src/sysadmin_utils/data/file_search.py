from pathlib import Path
from typing import Generator

try:
    from ..utils.config import Colors
except ImportError:
    class Colors:
        RESET = '\033[39m'
        HEADER = '\033[95m'


def search_files(directory: Path, extension: str) -> Generator[Path, None, None]:
    """
    Searches for files with a specific extension in a directory recursively.

    Args:
        directory (Path): The root directory to start searching from.
        extension (str): The file extension to look for (e.g., '.txt').

    Yields:
        Path: The path to each matching file found.
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
        target_dir_str = input("Directory to search: ")
        target_dir = Path(target_dir_str)
        ext = input("Extension (e.g., .py): ")

        found_any = False
        for file_path in search_files(target_dir, ext):
            print(f"Found: {file_path}")
            found_any = True

        if not found_any:
            print("No files found.")

    except KeyboardInterrupt:
        print("\nAborted.")
