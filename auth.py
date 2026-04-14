import hashlib
from getpass import getpass
from app.storage import load_data, save_data, destroy

def unlock():
    path = "data/profiles.json"
    profile = load_data(path)

    if not profile:
        print("No vault found!")
        return False
    
    p1 = profile[0]["master_key"]

    tries = 0
    while tries < 3:
        
        master_key = getpass("\nEnter master key: ")
        hashed_key = hashlib.sha256(master_key.encode()).hexdigest()
        
        if hashed_key == p1:
            print("Unlocked")
            return True
        tries += 1
        print("Invalid master key! Try again\n\033[31mAfter 3 invalid tries the system self-distructs!\033[0m")
        
    print("Too many attempts. Locked.")
    destroy("/data/vault.json")
    return False

unlock()