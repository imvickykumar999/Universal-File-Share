
# unzip /home/imvickykumar999/mysite/input.zip

import requests
username = 'imvickykumar999'

with open('API_Token.txt', 'r') as f:
    token = f.read()

def CPU_quota():
    response = requests.get(
        'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
            username=username
        ),
        headers={'Authorization': 'Token {token}'.format(token=token)}
    )
    if response.status_code == 200:
        print('CPU quota info:')
        print(response.content)
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

# CPU_quota()
