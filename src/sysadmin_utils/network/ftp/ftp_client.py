import ftplib  # nosec B402
from pathlib import Path
from typing import List


class FTPClient:
    """
    A simple FTP client for uploading and downloading files.
    """
    def __init__(self, host: str, user: str, password: str):
        self.host = host
        self.user = user
        self.password = password
        self.ftp = None

    def connect(self):
        """Establishes connection to the FTP server."""
        try:
            self.ftp = ftplib.FTP(self.host, self.user, self.password)  # nosec B321
            self.ftp.encoding = "utf-8"
            print(f"Connected to {self.host}")
        except Exception as e:
            print(f"Error connecting to FTP: {e}")
            raise

    def list_files(self) -> List[str]:
        """Lists files in the current directory."""
        if not self.ftp:
            self.connect()
        try:
            return self.ftp.nlst()
        except Exception as e:
            print(f"Error listing files: {e}")
            return []

    def upload_file(self, local_path: str, remote_filename: str = None):
        """Uploads a local file to the FTP server."""
        if not self.ftp:
            self.connect()

        local_path_obj = Path(local_path)
        if not local_path_obj.exists():
            print(f"File not found: {local_path_obj}")
            return

        remote_filename = remote_filename or local_path_obj.name

        try:
            with open(local_path_obj, "rb") as file:
                self.ftp.storbinary(f"STOR {remote_filename}", file)
            print(f"Uploaded {local_path_obj} to {remote_filename}")
        except Exception as e:
            print(f"Error uploading file: {e}")

    def download_file(self, remote_filename: str, local_path: str = None):
        """Downloads a file from the FTP server."""
        if not self.ftp:
            self.connect()

        local_path = local_path or remote_filename

        try:
            with open(local_path, "wb") as file:
                self.ftp.retrbinary(f"RETR {remote_filename}", file.write)
            print(f"Downloaded {remote_filename} to {local_path}")
        except Exception as e:
            print(f"Error downloading file: {e}")

    def close(self):
        """Closes the FTP connection."""
        if self.ftp:
            try:
                self.ftp.quit()
            except Exception:
                self.ftp.close()
            print("FTP connection closed.")


if __name__ == "__main__":
    # Example usage (Test server credentials from original script)
    HOST = "ftp.dlptest.com"
    USER = "dlpuser@dlptest.com"
    PASS = "SzMf7rTE4pCrf9dV286GuNe4N"

    client = FTPClient(HOST, USER, PASS)
    try:
        client.connect()
        print(client.list_files())
    except Exception:
        pass
    finally:
        client.close()
