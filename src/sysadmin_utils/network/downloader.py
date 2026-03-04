import urllib.request
import urllib.error


def download_file(url: str, filename: str):
    """
    Downloads a file from a URL.
    """
    print(f"Downloading from {url}...")
    try:
        urllib.request.urlretrieve(url, filename)  # nosec B310
        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Error downloading file: {e}")


if __name__ == "__main__":
    # Example usage
    test_url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
    download_file(test_url, "google_logo.png")
