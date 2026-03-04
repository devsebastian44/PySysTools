from winotify import Notification, audio
from pathlib import Path

# Define asset path relative to this file
ASSETS_DIR = Path(__file__).parent / "assets"
ICON_PATH = ASSETS_DIR / "icon.png"


def send_notification(title: str, message: str, app_id: str = "PySysTools",
                      action_label: str = None, action_link: str = None) -> None:
    """
    Sends a Windows Toast notification.

    Args:
        title (str): Title of the notification.
        message (str): Body text.
        app_id (str): Application Identifier.
        action_label (str, optional): Label for the action button.
        action_link (str, optional): URL or path to open when button is clicked.
    """
    try:
        icon = str(ICON_PATH) if ICON_PATH.exists() else ""

        toast = Notification(
            app_id=app_id,
            title=title,
            msg=message,
            duration="short",
            icon=icon
        )

        toast.set_audio(audio.Default, loop=False)

        if action_label and action_link:
            toast.add_actions(label=action_label, launch=action_link)

        toast.show()

    except ImportError:
        print("Error: 'winotify' is not installed. Please install it via pip.")
    except Exception as e:
        print(f"Failed to send notification: {e}")


if __name__ == "__main__":
    send_notification(
        title="Test Notification",
        message="This is a test from PySysTools.",
        action_label="Open Google",
        action_link="https://google.com"
    )
