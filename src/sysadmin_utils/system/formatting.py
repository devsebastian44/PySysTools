import shutil
import time
from pathlib import Path
from typing import Dict

# Extension mapping
EXTENSIONS: Dict[str, str] = {
    "jpg": "images", "jpeg": "images", "png": "images", "ico": "images",
    "gif": "images", "svg": "images",
    "sql": "sql",
    "exe": "programs", "msi": "programs",
    "pdf": "pdf",
    "xlsx": "excel", "csv": "excel",
    "rar": "archive", "zip": "archive", "gz": "archive", "tar": "archive",
    "docx": "word",
    "torrent": "torrent",
    "txt": "text",
    "ipynb": "python", "py": "python",
    "pptx": "powerpoint", "ppt": "powerpoint",
    "mp3": "audio", "wav": "audio",
    "mp4": "video", "m3u8": "video", "webm": "video", "ts": "video",
    "json": "json",
    "css": "web", "js": "web", "html": "web",
    "apk": "apk",
    "sqlite3": "sqlite3",
    "iso": "iso",
}


def organize_directory(path: Path, verbose: bool = False):
    """
    Organizes files in the specified directory into subfolders based on extensions.
    """
    path = Path(path)
    if not path.exists():
        print(f"Error: Path {path} does not exist.")
        return

    print(f" Organizing directory: {path}")

    # Iterate over all files in the directory
    for file_path in path.iterdir():
        if file_path.is_file():
            # Get extension without dot
            extension = file_path.suffix.lower().lstrip('.')

            if extension in EXTENSIONS:
                folder_name = EXTENSIONS[extension]
                target_folder = path / folder_name

                # Create folder if it doesn't exist
                target_folder.mkdir(exist_ok=True)

                # Move file
                target_path = target_folder / file_path.name
                try:
                    shutil.move(str(file_path), str(target_path))
                    if verbose:
                        print(f"Moved {file_path.name} -> {folder_name}/")
                except Exception as e:
                    print(f"Error moving {file_path.name}: {e}")


def watch_directory(path: Path, interval: int = 5):
    """
    Continuously watches and organizes a directory.
    """
    print(f"Watching {path} every {interval} seconds... (Ctrl+C to stop)")
    try:
        while True:
            organize_directory(path)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopping watch.")


if __name__ == "__main__":
    import sys

    # Get directory from args or input
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        target_dir = input("Directory to organize: ").strip()

    if target_dir:
        organize_directory(Path(target_dir), verbose=True)
    else:
        print("No directory specified.")
