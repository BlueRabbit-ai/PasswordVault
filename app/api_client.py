import requests


class ApiEntry:
    def __init__(self, site, username, password_hash):
        super().__init__(site, username, password_hash)


    def check_pawned(self):
        prefix = self.password_hash[:5]
        suffix = self.password_hash[5:]


        url = f"https://api.pwnedpasswords.com/range/{prefix}"

        try:
            res = requests.get(url)
            res.raise_for_status()

        except requests.exceptions.Timeout:
            print("Timed out")
        except requests.exceptions.ConnectionError as e:
            print(f"Connection failed {e}")
        except requests.exceptions.HTTPError as e:
            print(f"Bad HTTP response {e}")
        






