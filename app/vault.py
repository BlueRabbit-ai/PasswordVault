import re

class VaultEntry:
    def __init__(self, site: str, username: str) -> None:
        self.site = site
        self.username = username
        
    @property
    def username(self) -> str: # username getter
        return self._username
    
    @username.setter # username setter
    def username(self, username: str) -> None: #validatig username/no whitespace
        if not username.strip():
            raise ValueError("Field 'username' must be a non-empty string of min. 5 characters")
        elif len(username.strip()) < 5:
            raise ValueError("Username must be at least 5 characters long")
        self._username = username

    @property
    def site(self) -> str:
        return self._site
    
    @site.setter
    def site(self, site: str) -> None:
        if not site.strip():
            raise ValueError("Field 'site' should be a non-empty string")
        elif not self.validate_site(site):
            raise ValueError("Invalid site format")
        self._site = site

    @staticmethod
    def validate_site(site: str) -> bool:
        pattern = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
        return re.fullmatch(pattern, site) is not None

    
    def __str__(self) -> str:
        return f"username : {self.username}"
    
    def __repr__(self):
        return f"VaultEntry('site'= {self.site}, 'username': {self.username},)"
    

# print(hashlib.sha256("Password".encode()).hexdigest())
    

