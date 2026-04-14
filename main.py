from app.api_client import ApiEntry
from app.storage import load_data, save_data, data_path
from auth import unlock


def load_entries():
    raw = load_data(data_path)
    entries = []

    for item in raw:
        entry = ApiEntry.from_dict(item)
        if entry:
            entries.append(entry)

    return entries


def save_entries(entries):
    data = [e.to_dict() for e in entries]
    save_data(data, data_path)


def menu():
    print("\n=== VAULT MENU ===")
    print("1. Add entry")
    print("2. View entries")
    print("3. Delete entry")
    print("4. Check password (HIBP)")
    print("5. Exit")


def main():
    if not unlock():
        return

    entries = load_entries()

    while True:
        menu()
        choice = input("Select option: ")

        if choice == "1":
            site = input("Site: ")
            username = input("Username: ")
            password = input("Password: ")

            try:
                entry = ApiEntry(site, username, password)
                entries.append(entry)
                print("Entry added.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            if not entries:
                print("Vault is empty.")
                continue

            for i, e in enumerate(entries):
                print(f"{i}: {e}")

        elif choice == "3":
            index = input("Enter index to delete: ")

            if not index.isdigit():
                print("Invalid input.")
                continue

            index = int(index)

            if 0 <= index < len(entries):
                removed = entries.pop(index)
                print(f"Deleted: {removed.site}")
            else:
                print("Invalid index.")

        elif choice == "4":
            index = input("Enter index to check: ")

            if not index.isdigit():
                print("Invalid input.")
                continue

            index = int(index)

            if 0 <= index < len(entries):
                entries[index].check_pawned()
            else:
                print("Invalid index.")

        elif choice == "5":
            save_entries(entries)
            print("Vault saved. Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()