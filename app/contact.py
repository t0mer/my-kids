import requests
from dataclasses import dataclass, field

@dataclass
class Contact:
    id: str
    server: str
    name: str
    isUser: bool
    isGroup: bool
    isMyContact: bool
    isWAContact: bool
    isBusiness: bool
    download_media: bool = field(default=False)
    
