class PeopleService:

    def __init__(self, client):
        self.client = client

    def get_all_people(self):

        payload = {
            "IdsPessoa": [0],
            "MarcacaoColetadaAPI": False,
            "ResponseType": "AS400V1"
        }

        return self.client.post(
            "People/SearchPeople",
            payload
        )