import requests
import re

TOKEN = 'SbZTSgucxZn5Md9gZ0YxZIZO1OgX4zic'
API_URL = 'https://api.apilayer.com/temp_mail'


class TempMail:
    def __init__(self):
        self.url = API_URL
        self.email = str()
        self.password = str()
        # self.token = TOKEN
        # self.id = str()
        self.message_id = str()
        self.header = {
            'apikey': f'{TOKEN}'
        }

    def get_domains(self):
        req_url = self.url + '/domains'
        response = requests.request("GET", req_url, headers=self.header)
        return response.text
