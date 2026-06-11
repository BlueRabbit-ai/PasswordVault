import json
from pathlib import Path

_base = Path(__file__).resolve().parent.parent  # project root
_data_dir = _base / "data"
data_path = _data_dir / "vault.json"
profile_path = _data_dir / "profiles.json"


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


