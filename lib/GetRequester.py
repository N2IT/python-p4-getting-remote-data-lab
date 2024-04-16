import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = self.url

        response = requests.get(URL)
        return response.content

    def load_json(self):
        python_list = []
        responses = json.loads(self.get_response_body())
        for response in responses:
            python_list.append(response)
        
        return python_list

