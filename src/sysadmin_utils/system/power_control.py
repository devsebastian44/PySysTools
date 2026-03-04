import os


def shutdown_system(delay: int = 60):
    """
    Schedules a system shutdown.
    """
    print(f"System will shutdown in {delay} seconds.")
    if os.name == "nt":
        os.system(f"shutdown /s /t {delay}")
    else:
        os.system(f"sudo shutdown -h +{delay // 60}")


def cancel_shutdown():
    """
    Cancels a scheduled shutdown.
    """
    print("Canceling scheduled shutdown...")
    if os.name == "nt":
        os.system("shutdown /a")
    else:
        os.system("sudo shutdown -c")


if __name__ == "__main__":
    # WARNING: Be careful when running this script
    print("Shutdown controller (Test mode)")
    # cancel_shutdown() # Just to be safe