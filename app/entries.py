from app.vault import VaultEntry
import hashlib
import datetime


class PasswordEntry(VaultEntry):
    def __init__(self, site: str, username: str, password: str) -> None:
        self._set_password(password)
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super().__init__(site, username)

    def __str__(self):
        return f"PasswordEntry('site': {self.site}, 'username': {self.username}, 'password_hash': {self.password_hash})"

    def _set_password(self, password: str):
        if not password.strip():
            raise ValueError("Password cannot be empty")

        self._password_hash = hashlib.sha256(password.encode()).hexdigest()
        self._sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()

    @property
    def password_hash(self):
        return self._password_hash

    @property
    def sha1_hash(self):
        return self._sha1_hash

    def to_dict(self):
        return {
            "site": self.site,
            "username": self.username,
            "password_hash": self.password_hash
        }

    @classmethod
    def from_dict(cls, my_dict):
        try:
            obj = cls.__new__(cls)
            obj.site = my_dict["site"]
            obj.username = my_dict["username"]
            obj._password_hash = my_dict["password_hash"]
            obj._sha1_hash = None
            obj.created_at = None
            return obj
        except KeyError:
            print("Invalid dictionary format")
            return None