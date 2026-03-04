import os


def shutdown_system(delay: int = 60):
    """
    Schedules a system shutdown.
    """
    print(f"System will shutdown in {delay} seconds.")
    import subprocess
    if os.name == "nt":
        subprocess.run(["shutdown", "/s", "/t", str(delay)], shell=False)
    else:
        subprocess.run(["sudo", "shutdown", "-h", f"+{delay // 60}"], shell=False)


def cancel_shutdown():
    """
    Cancels a scheduled shutdown.
    """
    print("Canceling scheduled shutdown...")
    import subprocess
    if os.name == "nt":
        subprocess.run(["shutdown", "/a"], shell=False)
    else:
        subprocess.run(["sudo", "shutdown", "-c"], shell=False)


if __name__ == "__main__":
    # WARNING: Be careful when running this script
    print("Shutdown controller (Test mode)")
    # cancel_shutdown() # Just to be safe
