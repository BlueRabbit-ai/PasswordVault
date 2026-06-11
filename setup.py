import hashlib
from getpass import getpass
from app.storage import save_data, profile_path, data_path as vault_path


def setup():
    print("=== Vault Setup ===")

    # Ensure directories exist
    profile_path.parent.mkdir(parents=True, exist_ok=True)
    vault_path.parent.mkdir(parents=True, exist_ok=True)

    # If profile already exists → warn user
    if profile_path.exists():
        print("\nA profile already exists.")
        confirm = input("This will OVERWRITE your profile and vault. Type 'YES' to continue: ").upper()

        if confirm != "YES":
            print("Setup cancelled.")
            return False

    # Create master password
    while True:
        p1 = getpass("Create master password: ")
        p2 = getpass("Confirm master password: ")

        if p1 != p2:
            print("Passwords do not match.\n")
            continue

        if not p1.strip():
            print("Password cannot be empty.\n")
            continue

        if len(p1) < 5:
            print("Password must be at least 5 characters.\n")
            continue

        break

    # Hash password (SHA-256)
    hashed = hashlib.sha256(p1.encode()).hexdigest()

    # Save profile
    save_data([{"master_key": hashed}], profile_path)

    # Warn before wiping vault
    print("\nWARNING: This will DELETE ALL vault entries!")
    confirm = input("Type 'DELETE' to confirm: ")

    if confirm == "DELETE":
        save_data([], vault_path)
        print("Vault cleared.")
    else:
        print("Vault NOT cleared.")

    print("\nSetup complete. You can now use the vault.")
    return True


if __name__ == "__main__":
    setup()