from vault import VaultEnry
from api_client import ApiEntry
import hashlib
import datetime

class PasswordEntry(VaultEnry):
    def __init__(self,site: str, username: str, password_hash:str, ) -> None:
        self._password_hash = hashlib.sha256(password_hash.encode()).hexdigest()
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super().__init__(site, username)

    @property
    def password_hash(self):
        return self._password
    
    
    @password_hash.setter
    def password_hash(self, password_hash):
        if not password_hash.strip():
            raise ValueError("Field 'password' must be a non-empty string")
        self._password_hash = password_hash

    def new_password(self):
        pass

    def to_dict(self):
        return {
            "site": self.site,
            "username": self.username,
            "password_hash": self.password_hash
        }



print(hashlib.sha256("Password".encode()).hexdigest())[:5]