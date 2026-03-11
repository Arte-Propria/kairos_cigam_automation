import requests
import json

class KairosClient:

    BASE_URL = "https://www.dimepkairos.com.br/RestServiceApi"

    def __init__(self, identifier, key):

        self.headers = {
            "identifier": identifier,
            "key": key,
            "Accept": "*/*",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            "Content-Type": "application/json"
        }

    def post(self, endpoint, payload):

        url = f"{self.BASE_URL}/{endpoint}"

        response = requests.post(
            url,
            headers=self.headers,
            data=json.dumps(payload)
        )

        print("\n================ DEBUG RESPONSE ================")
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)
        print("===============================================")

        response.raise_for_status()

        return response.json()