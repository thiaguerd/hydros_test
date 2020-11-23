from urllib.parse import urlencode
from django.conf import settings

import requests
import json


class Google:
    @staticmethod
    def url_in():
        base = settings.SOCIAL_PROVIDERS['google']['url']['login']
        params = urlencode(settings.SOCIAL_PROVIDERS['google']['params_login'])
        return base + "?" + params

    @staticmethod
    def auth(code):
        uri = settings.SOCIAL_PROVIDERS['google']['url']['auth']
        auth = settings.SOCIAL_PROVIDERS['google']['auth_params']
        auth['code'] = code
        auth['redirect_uri'] = 'http://localhost:8000/callback'
        response = requests.post(uri, data=json.dumps(auth), headers={"content-type": "application/json"})
        data = json.loads(response.text)
        data['status'] = response.status_code
        return data

    @staticmethod
    def info(auth):
        uri = settings.SOCIAL_PROVIDERS['google']['url']['info']
        uri += "?access_token=" + auth['access_token']
        return json.loads(requests.get(uri).text)
