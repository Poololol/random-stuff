import requests
from base64 import b64encode
def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'
header = {'Content-Type': 'application/json',
          'Ubi-AppId': '86263886-327a-4328-ac69-527f0d20a237',
          'Authorization': basic_auth('braedonegrillot@gmail.com', 'Tardis0306!')}
param = {'User-Agent': 'Get PB times and places / braedonegrillot@gmail.com'}
r = requests.post('https://public-ubiservices.ubi.com/v3/profiles/sessions', headers=header)
print(r.text)