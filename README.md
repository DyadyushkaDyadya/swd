# Steam Workshop Downloader
Simple Steam Workshop Downloader. Powered by MODSDOWNLOADER.COM

# Installing
```py
pip install swd
```

# Example using
```py
from swd import SteamWorkshopItem
item = SteamWorkshopItem('https://steamcommunity.com/sharedfiles/filedetails/?id=2971831945')

if item.status == 1:
    print(f"ID: {item.id}")
    print(f"Game: {item.game}")
    print(f"Title: {item.title}")
    print(f"Image: {item.image}")
    print(f"Size: {item.size}")
    print(f"Download: {item.download}")
    print(f"Steam: {item.steam}")
else:
    print("Request failed")
```
