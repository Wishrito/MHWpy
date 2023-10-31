import requests

class MHWDBWrapper:
    def __init__(self):
        self.base_url = "https://mhw-db.com"

    # Fonctions partagées
    def make_request(self, endpoint: str):
        url = self.base_url + endpoint
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
