import requests
from app.entries import PasswordEntry

class ApiEntry(PasswordEntry):
    def __init__(self, site: str, username: str, password: str) -> None:
        super().__init__(site, username, password)

    def __str__(self):
        return f"{self.site} ({self.username})"


    def check_pwned(self):
        if not self.sha1_hash:
            print("Cannot check — SHA-1 hash not available (entry loaded from disk).")
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
        entry.check_pwned()

if __name__ == '__main__':
    main()
