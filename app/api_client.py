import requests
from app.entries import PasswordEntry

class ApiEntry(PasswordEntry):
    def __init__(self, site, username, password):
        super().__init__(site, username, password)


    def __str__(self):
        return f"ApiEntry('site': {self.site}, 'username': {self.username}, 'password_hash': {self.password_hash})"


    def check_pawned(self):
        if not self.sha1_hash:
            print("Cannot check stored (hashed-only) password.")
            return None
        
        prefix = self.sha1_hash[:5].upper()
        suffix = self.sha1_hash[5:].upper()


        url = f"https://api.pwnedpasswords.com/range/{prefix}"

        try:
            res = requests.get(url, timeout=3)
            res.raise_for_status()

        except requests.exceptions.Timeout:
            print("Request timed out")
            return None
        
        except requests.exceptions.ConnectionError:
            print("Connection failed")
            return None

        except requests.exceptions.HTTPError as e:
            print(f"Bad HTTP response {e}")
            return None
        
        except requests.exceptions.RequestException as e:
            print(f"Unexpected request error: {e}")
            return None
        
        hashes = (line.split(":") for line in res.text.splitlines())

        for h, count in hashes:
            if h.strip().upper() == suffix:
                print(f"Password found {count} times!")
                return int(count)
        
        print("Password not found in breaches.")
        return 0
    
    def to_dict(self):
        return {
            "site": self.site,
            "username": self.username,
            "password_hash": self.password_hash
        }
    
    @classmethod
    def from_dict(cls, my_dict):
        try:
            obj = cls.__new__(cls)  # bypass __init__
            obj.site = my_dict["site"]
            obj.username = my_dict["username"]
            obj._password_hash = my_dict["password_hash"]
            obj._sha1_hash = None  # can't recover
            return obj
        except KeyError:
            print("Error! Make sure your dictionary has this keys: 'site', 'username', 'password_hash'")

def main():
    # testing api
    tests = [
        "password",
        "123456",
        "passwoerd123",
        "XyZ!9KjdshhiHDIUW?&%Hkhdanafkjn"
    ]

    for test in tests:
        print(f"Testing: {test}")
        entry = ApiEntry("test.com", "user123", test)
        entry.check_pawned()

if __name__ == '__main__':
    main()







