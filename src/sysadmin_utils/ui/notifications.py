try:
    from winotify import Notification, audio
except ImportError:
    # Handle non-windows or missing dependency
    Notification = None
    audio = None


def send_windows_notification(title: str, msg: str, duration: str = "short"):
    """
    Sends a native Windows toast notification.
    """
    if not Notification:
        print(f"Notification (CLI): {title} - {msg}")
        return

    toast = Notification(
        app_id="PySysTools",
        title=title,
        msg=msg,
        duration=duration
    )
    toast.set_audio(audio.Default, loop=False)
    toast.show()


if __name__ == "__main__":
    send_windows_notification("Test Alert", "This is a PySysTools notification!")
