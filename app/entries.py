from vault import VaultEntry
import hashlib
import datetime

class PasswordEntry(VaultEntry):
    def __init__(self,site: str, username: str, password:str, ) -> None:
        self._set_password(password)
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super().__init__(site, username)

    def _set_password(self, password: str):
        if not password.strip():
            raise ValueError("Password cannot be empty")
        
        self._password_hash = hashlib.sha256(password.encode()).hexdigest() # store in sha256
        self._sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper() # only for api check

    @property
    def password_hash(self):
        return self._password_hash
    
    @property
    def sha1_hash(self):
        return self._sha1_hash
    

    def new_password(self):
        pass

    def to_dict(self):
        return {
            "site": self.site,
            "username": self.username,
            "password_hash": self.password_hash
        }

