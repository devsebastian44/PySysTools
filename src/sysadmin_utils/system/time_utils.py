import os
import time
from datetime import datetime


def modify_file_time(path: str, date_str: str):
    """
    Modifies the access and modification time of a file or folder.
    Format: 'YYYY-MM-DD HH:MM:SS'
    """
    if not os.path.exists(path):
        print(f"Error: {path} not found.")
        return

    try:
        # Convert string to epoch time
        dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        epoch = time.mktime(dt.timetuple())

        # Update times
        os.utime(path, (epoch, epoch))
        print(f"Successfully updated timestamp for {path} to {date_str}")
    except ValueError:
        print("Error: Invalid date format. Use 'YYYY-MM-DD HH:MM:SS'")
    except Exception as e:
        print(f"Error modifying time: {e}")


if __name__ == "__main__":
    # List files in current directory to help user
    print("Current files:")
    for f in os.listdir("."):
        print(f" - {f}")

    target = input("\nEnter file or folder name: ").strip()
    new_date = input("Enter new date (YYYY-MM-DD HH:MM:SS): ").strip()

    if target and new_date:
        modify_file_time(target, new_date)
