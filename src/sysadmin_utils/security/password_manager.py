import string
import secrets


try:
    from ..utils.config import Colors
except ImportError:
    # Fallback if run directly without package context
    class Colors:
        GREEN = '\033[32m'
        RESET = '\033[39m'
        HEADER = '\033[95m'


def generate_password(length: int = 16, use_symbols: bool = True) -> str:
    """
    Generates a cryptographically secure password.

    Args:
        length (int): Length of the password.
        use_symbols (bool): Whether to include special symbols.

    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += "[]{}()*;/,._-!$%?@#"

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def save_password(password: str, file_path: str = "clave.key") -> None:
    """Saves the password to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(password)
        print(f"{Colors.GREEN}Password saved to {file_path}{Colors.RESET}")
    except IOError as e:
        print(f"Error saving password: {e}")


if __name__ == "__main__":
    print(f"{Colors.HEADER}--- Secure Password Generator ---{Colors.RESET}")

    try:
        length_input = input("Enter password length (default 16): ")
        pw_length = int(length_input) if length_input else 16
    except ValueError:
        pw_length = 16
        print("Invalid input, using default length 16.")

    pwd = generate_password(pw_length)
    print(f"\nGenerated Password: {Colors.GREEN}{pwd}{Colors.RESET}")

    save = input("Save to file 'clave.key'? (y/n): ").lower()
    if save == 'y':
        save_password(pwd)