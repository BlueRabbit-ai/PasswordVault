import json
from pathlib import Path

base = Path(__file__).resolve().parent
data_path = base.parent / "data" / "vault.json"

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
        
    except FileNotFoundError:
        return []
    
def save_data(data, filepath="/data/vault.json"):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def destroy(filepath):
    with open(filepath, "w") as f:
        f.write([])

def delete():
    data = load_data("/data/vault.json")
    # remove = 
