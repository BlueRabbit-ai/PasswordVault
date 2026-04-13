import requests
from entries import PasswordEntry

class ApiEntry:
    def __init__(self, site, username, password):
        super().__init__(site, username, password)


    def check_pawned(self):
        prefix = self.password_hash[:5]
        suffix = self.password_hash[5:].upper()


        url = f"https://api.pwnedpasswords.com/range/{prefix}"

        try:
            res = requests.get(url)
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
            if h == suffix:
                print(f"Password found {count} times!")
                return int(count)
        
        print("Password not found in breaches.")
        return 0
        
d = ApiEntry("github.com", "bluerabbit@icloud.com", "password")
d.check_pawned()







