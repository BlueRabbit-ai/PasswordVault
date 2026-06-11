import hashlib
from getpass import getpass
from app.storage import load_data, profile_path
from setup import setup


def _ensure_profile():
    """Ensure a valid profile exists. Returns the profile data or None if setup was cancelled."""
    if not profile_path.exists():
        print("No profile found. Starting setup...\n")
        if not setup():
            return None

    profile = load_data(profile_path)

    if not profile:
        print("Profile corrupted. Recreating...")
        if not setup():
            return None
        profile = load_data(profile_path)

    if not profile:
        print("Failed to create profile.")
        return None

    return profile


def unlock():
    profile = _ensure_profile()
    if profile is None:
        print("Cannot unlock without a profile. Exiting.")
        return False

    stored_hash = profile[0]["master_key"]

    tries = 0
    while tries < 3:
        master_key = getpass("\nEnter master key: ")
        hashed_key = hashlib.sha256(master_key.encode()).hexdigest()

        if hashed_key == stored_hash:
            print("Unlocked")
            return True

        tries += 1
        remaining = 3 - tries
        if remaining > 0:
            print(f"Invalid master key! {remaining} attempt(s) remaining.")

    # Too many tries — lock out, do NOT wipe
    print("\nToo many failed attempts. Access denied.")
    return False