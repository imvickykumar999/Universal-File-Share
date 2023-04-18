
# unzip /home/imvickykumar999/mysite/input.zip

from urllib.parse import urljoin
import requests


username = 'imvickykumar999'
pythonanywhere_host = "www.pythonanywhere.com"

with open('API_Token.txt', 'r') as f:
    api_token = f.read()

api_base = "https://{pythonanywhere_host}/api/v0/user/{username}/".format(
    pythonanywhere_host=pythonanywhere_host,
    username=username,
)


def CPU_Quota():
    response = requests.get(
        'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
            username=username
        ),
        headers={'Authorization': 'Token {api_token}'.format(api_token=api_token)}
    )
    if response.status_code == 200:
        print('CPU quota info:')
        print(response.content)
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

# CPU_Quota()


def Listing_Files():
    resp = requests.get(
        urljoin(api_base, "files/path/home/{username}/mysite/input/".format(username=username)),
        headers={"Authorization": "Token {api_token}".format(api_token=api_token)}
    )

    print()
    for i,j in enumerate(list(resp.json().keys())):
        print(i+1, '). ', j)
    print()

# Listing_Files()


def Download_Files():
    Listing_Files()
    file = input('Enter File Name from above list : ')

    resp = requests.get(
        urljoin(api_base, f"files/path/home/{username}/mysite/input/{file}".format(username=username)),
        headers={"Authorization": "Token {api_token}".format(api_token=api_token)}
    )

    with open(f'Files/{file}', 'wb') as f:
        f.write(resp.content)

# Download_Files()

