from typing import Union

import requests
import re

API_URL = 'https://api.mail.tm'
# API_URL = 'https://api.mail.gw'

# https://docs.mail.tm/


class TempMail:
    def __init__(self, email_login: str, password: str):
        self.url = API_URL
        self.password = password
        self.token = str()
        self.id = str()
        self.email = str()
        self.message_id = str()
        self.__get_domains(email_login)

    # To get current available email domains. Need to use before create account
    def __get_domains(self, login_name: str):
        req_url = self.url + '/domains'
        response = requests.request("GET", req_url)
        self.email = f"{login_name}@" + response.json().get('hydra:member')[0].get('domain')
        # print(f'Domains list: {response.text}')
        # print(f'\n{self.email}\n')

    # Before using mail we need to create account
    def post_create_account(self) -> Union[str, int]:
        req_url = self.url + '/accounts'
        data = {
            "address": f"{self.email}",
            "password": f"{self.password}"
        }
        response = requests.request("POST", req_url, json=data)
        # print(f'Createion status: {response.status_code}\nResponse message: {response.text}')
        # Can't use the same email address
        if response.status_code != 201:
            return f'Smt went wrong. Status code: {response.status_code}\n' \
                   f'Error: {response.json().get("violations")[0].get("propertyPath")}: ' \
                   f'{response.json().get("violations")[0].get("message")}'
        # ID is needed for deleting account
        else:
            self.id = response.json().get('id')
            return response.status_code

    # Get auth token
    def post_auth(self):
        req_url = self.url + '/token'
        data = {
            "address": f"{self.email}",
            "password": f"{self.password}"
        }
        response = requests.request("POST", req_url, json=data)
        # print(response.text)
        if response.status_code == 401:
            return False
        else:
            # Token is used in every request except create account and get domains
            self.token = 'Bearer ' + f'{response.json().get("token")}'
            self.id = response.json().get('id')
            return True

    # Save id of the newest message
    def get_messages(self) -> bool:
        req_url = self.url + '/messages'
        header = {
            "Authorization": f"{self.token}"
        }
        response = requests.request("GET", req_url, headers=header)
        if response.status_code == 200:
            assert len(response.json().get('hydra:member')) > 0, f'The inbox is empty.\nLogin: "{self.email}", ' \
                                                                 f'password: "{self.password}"'
            self.message_id = response.json().get('hydra:member')[0].get('id')

    # Returns text of the newest message
    def get_message_by_id(self) -> str:
        req_url = self.url + f'/messages/{self.message_id}'
        header = {
            "Authorization": f"{self.token}"
        }
        response = requests.request("GET", req_url, headers=header)
        # print(f'get message by id response: {response.json()}')
        message = response.json().get('html')
        # print(f'get message by id message: {message}')
        return message

    # Returns the Account resource that matches the Bearer token that sent the request
    def get_me(self) -> bool:
        req_url = self.url + '/me'
        header = {
            "Authorization": f"{self.token}"
        }
        response = requests.request("GET", req_url, headers=header)
        email_ready = True
        print(response.text)
        for el in [response.json().get('isDisabled'), response.json().get('isDeleted')]:
            if el:
                email_ready = False
        return email_ready

    # Deletes account. Could be deleted after account del tests.
    def delete_account(self):
        req_url = self.url + '/accounts/' + f'{self.id}'
        header = {
            "Authorization": f"{self.token}"
        }
        response = requests.request("DELETE", req_url, headers=header)
        if response.status_code == 204:
            print("Account was deleted")
        else:
            # If smt went wrong we get err code
            print(response.status_code)

    # Gets code from email
    def parse_message(self) -> int:
        message = self.get_message_by_id()
        # message = message
        # print(f'parser_message: {message}')
        code_pattern = re.compile(r'>\d{6}<')
        code = code_pattern.findall(str(message))
        # print(f'pars msg code: {code}')
        return code[0][1:-1:]

# TODO: Возможно стоит возвращать в каждом запросе код и текст сообщения на случай падений
# TODO: Проверку на неправильные кредсы входа


# address = "user_7"
# password = "testsls2022"
# message = 'none; background-color: #ffffff; color: #718096; height: 100%; text-align: left;">400893</h1>\r\n<p style="box-sizing: border-box;'
# temp = TempMail(address, password)
# temp.post_auth()
# print(temp.get_messages())
# print(temp.parse_message(message))
# print(temp.post_create_account())
# print(temp.post_auth())
# print(temp.get_me())

