import hashlib
from pathlib import Path


try:
    from ..utils.config import Colors
except ImportError:
    class Colors:
        BLUE = '\033[34m'
        RESET = '\033[39m'
        HEADER = '\033[95m'
        RED = '\033[91m'
        GREEN = '\033[32m'


def calculate_file_hash(file_path: Path, algorithm: str = "sha256") -> str:
    """Calculates the hash of a file."""
    try:
        if algorithm == "sha256":
            hasher = hashlib.sha256()
        elif algorithm == "md5":
            hasher = hashlib.md5()
        else:
            raise ValueError("Unsupported algorithm")
            
        with open(file_path, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):
                hasher.update(block)
        return hasher.hexdigest()
    except FileNotFoundError:
        return ""


def compare_hash_with_list(file_hash: str, hash_list_path: Path) -> bool:
    """Checks if a hash exists in a file (one hash per line)."""
    if not hash_list_path.exists():
        print(f"Hash list not found: {hash_list_path}")
        return False
        
    try:
        with open(hash_list_path, 'r') as f:
            known_hashes = {line.strip() for line in f}
            
        return file_hash in known_hashes
    except Exception as e:
        print(f"Error reading hash list: {e}")
        return False


def interactive_check():
    """Interactive CLI for hash checking."""
    print(f"{Colors.BLUE}--- File Hash Checker ---{Colors.RESET}")
    
    file_path = input("Enter file path: ").strip()
    if not file_path:
        return
        
    path = Path(file_path)
    if not path.exists():
        print(f"{Colors.RED}File not found.{Colors.RESET}")
        return

    computed_hash = calculate_file_hash(path)
    print(f"\n{Colors.HEADER}SHA-256:{Colors.RESET} {computed_hash}")

    hash_db_input = input("Enter path to hash database (optional, press Enter to skip): ").strip()
    if hash_db_input:
        db_path = Path(hash_db_input)
        if compare_hash_with_list(computed_hash, db_path):
            msg = "[!] Hash found in database (Potentially Malicious)"
            print(f"{Colors.RED}{msg}{Colors.RESET}")
        else:
            msg = "[+] Hash not found in database."
            print(f"{Colors.GREEN}{msg}{Colors.RESET}")


if __name__ == "__main__":
    interactive_check()
