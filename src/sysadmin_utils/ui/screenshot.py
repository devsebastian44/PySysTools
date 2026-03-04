import pyautogui
import time
from pathlib import Path


def take_screenshot(output_path: str):
    """
    Takes a single screenshot and saves it to the specified path.
    """
    try:
        # Pyscreeze (used by pyautogui) might need explicit path handling
        output_path = str(Path(output_path).resolve())
        print("Taking screenshot in 2 seconds...")
        time.sleep(2)
        screenshot = pyautogui.screenshot()
        screenshot.save(output_path)
        print(f"Screenshot saved to {output_path}")
    except Exception as e:
        print(f"Error taking screenshot: {e}")


if __name__ == "__main__":
    take_screenshot("screenshot_test.png")
