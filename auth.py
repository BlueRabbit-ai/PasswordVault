import hashlib
from getpass import getpass
from pathlib import Path
from app.storage import load_data, destroy, data_path
from setup import setup  # import setup

profile_path = Path("data/profiles.json")


def unlock():
    # If no profile → run setup
    if not profile_path.exists():
        print("No profile found. Starting setup...\n")
        setup()

    profile = load_data(profile_path)

    if not profile:
        print("Profile corrupted. Recreating...")
        setup()
        profile = load_data(profile_path)

    stored_hash = profile[0]["master_key"]

    tries = 0
    while tries < 3:
        master_key = getpass("\nEnter master key: ")
        hashed_key = hashlib.sha256(master_key.encode()).hexdigest()

        if hashed_key == stored_hash:
            print("Unlocked")
            return True

        tries += 1
        print("Invalid master key!")

    # Too many tries → WIPE + RESET
    print("\nToo many attempts!")
    print("Vault will be wiped and reset.\n")

    destroy(data_path)

    # FORCE NEW SETUP
    setup()

    return True  # allow app to continue after reset