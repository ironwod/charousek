import requests as req


class LichessConnector:
    def __init__(self, token_fp=""):
        self.user_url = "https://lichess.org/api/account"
        self.games_url = "https://lichess.org/api/games/user"
        self.puzzle_url = "https://lichess.org/api/puzzle/activity"
        self.api_token = self._read_api_token(token_fp)
        self.headers = {
            "Authorization": f"Bearer {self.api_token}"
        }
        self.username = self.get_username()

    
    def read_games(self):
        pass
        
    
    def get_username(self):
        resp = req.get(self.user_url, headers=self.headers)
        if resp.status_code != 200:
            raise Exception(f"Invalid Response: {resp.status_code}")
        return resp.json()["username"]

    @staticmethod
    def _read_api_token(token_file_path):
        with open(token_file_path, "r") as f:
            token = f.read().strip()
        return token

