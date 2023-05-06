import requests

class SteamWorkshopItem:
    def __init__(self, url):
        self.url = url
        self.status = None
        self.id = None
        self.game = None
        self.title = None
        self.image = None
        self.size = None
        self.download = None
        self.steam = None
        self.send_request()

    def send_request(self):
        api_url = 'https://modsdownloader.com/api/' + self.url

        response = requests.get(api_url)
        data = response.json()
        if 'status' in data:
            self.status = data['status']
        if 'result' in data:
            result = data['result']
            if isinstance(result, list):
                if len(result) > 0:
                    item_data = result[0]
                    self.id = item_data.get('id')
                    self.game = item_data.get('game')
                    self.title = item_data.get('title')
                    self.image = item_data.get('image')
                    self.size = item_data.get('size')
                    self.download = item_data.get('download')
                    self.steam = item_data.get('steam')
            else:
                self.id = result.get('id')
                self.game = result.get('game')
                self.title = result.get('title')
                self.image = result.get('image')
                self.size = result.get('size')
                self.download = result.get('download')
                self.steam = result.get('steam')

        return data