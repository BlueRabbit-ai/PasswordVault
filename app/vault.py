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
        stripped = site.strip()
        if not stripped:
            raise ValueError("Field 'site' must be a non-empty string")
        if not self.validate_site(stripped):
            raise ValueError("Invalid site format")
        self._site = stripped

    @staticmethod
    def validate_site(site: str) -> bool:
        # Accept domains, IPs, localhost, with optional http(s):// prefix
        pattern = (
            r"((http|https)://)?"                              # optional scheme
            r"("
            r"([a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?\.)+"   # domain labels with dots
            r"([a-zA-Z]{2,})"                                   # TLD (2+ letters)
            r"|"
            r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"            # IPv4
            r"|"
            r"(localhost)"                                       # localhost
            r")"
            r"(:\d+)?"                                          # optional port
            r"(/[a-zA-Z0-9.\-_~:/?#\[\]@!$&'()*+,;=]*)?"       # optional path/query/fragment
        )
        return re.fullmatch(pattern, site) is not None

    
    def __str__(self) -> str:
        return f"site: {self.site}, username: {self.username}"

    def __repr__(self):
        return f"VaultEntry('site'={self.site!r}, 'username'={self.username!r})"

