from vault import VaultEntry
import hashlib
import datetime

class PasswordEntry(VaultEntry):
    def __init__(self,site: str, username: str, password:str, ) -> None:
        self.password = password
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super().__init__(site, username)

    @property
    def password_hash(self):
        return self._password_hash
    
    @property
    def password(self):
        return ArithmeticError("Password cannot be read directly")
    @password.setter
    def password(self, password: str):
        if not password.strip():
            raise ValueError("Password cannot be emoty")
        self._password_hash = hashlib.sha256(password.encode()).hexdigest()


    def new_password(self):
        pass

    def to_dict(self):
        return {
            "site": self.site,
            "username": self.username,
            "password_hash": self.password_hash
        }

