import json
from pathlib import Path

base = Path(__file__).resolve().parent
data_path = base.parent / "data" / "vault.json"


def load_data(filepath=data_path):
    filepath = Path(filepath)

    try:
        with open(filepath, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)

    except FileNotFoundError:
        return []


def save_data(data, filepath=data_path):
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def destroy(filepath=data_path):
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, "w") as f:
        json.dump([], f, indent=2)


def delete(index: int):
    data = load_data(data_path)

    if not data:
        print("Vault is empty")
        return False

    if index < 0 or index >= len(data):
        print("Invalid index")
        return False

    removed = data.pop(index)
    save_data(data, data_path)

    print(f"Deleted entry: {removed['site']} ({removed['username']})")
    return True