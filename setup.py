import hashlib
from getpass import getpass
from app.storage import save_data
import json
from pathlib import Path

profile_path = Path("data/profiles.json")
vault_path = Path("data/vault.json")


def setup():
    print("=== Vault Setup ===")

    if profile_path.exists():
        print("\nA profile already exists.")
        confirm = input("This will OVERWRITE your vault. Type 'YES' to continue: ")

        if confirm != "YES":
            print("Setup cancelled.")
            return

    while True:
        p1 = getpass("Create master password: ")
        p2 = getpass("Confirm master password: ")

        if p1 != p2:
            print("Passwords do not match. Try again.\n")
            continue

        if not p1.strip():
            print("Password cannot be empty.\n")
            continue

        break

    hashed = hashlib.sha256(p1.encode()).hexdigest()

    # Save profile
    save_data([{"master_key": hashed}], profile_path)

    # WIPE VAULT
    print("\nWARNING: All existing vault entries will be deleted!")
    confirm = input("Type 'DELETE' to confirm: ")

    if confirm == "DELETE":
        save_data([], vault_path)
        print("Vault cleared.")
    else:
        print("Vault NOT cleared.")

    print("Setup complete.")