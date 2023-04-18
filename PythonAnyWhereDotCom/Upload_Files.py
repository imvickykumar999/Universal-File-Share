
# unzip /home/imvickykumar999/mysite/input.zip

from urllib.parse import urljoin
import requests


username = 'imvickykumar999'
pythonanywhere_host = "www.pythonanywhere.com"
api_base = f"https://{pythonanywhere_host}/api/v0/user/{username}/"

with open('API_Token.txt', 'r') as f:
    api_token = f.read() # file is in .gitignore


def CPU_Quota():
    response = requests.get(
        f'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/',
        headers={'Authorization': f'Token {api_token}'}
    )
    if response.status_code == 200:
        print('CPU quota info:')
        print(response.content)
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

# CPU_Quota()


def List_Files():
    resp = requests.get(
        urljoin(api_base, f"files/path/home/{username}/mysite/input/"),
        headers={"Authorization": f"Token {api_token}"}
    )

    print()
    for i,j in enumerate(resp.json().keys()):
        print(i+1, '). ', j)
    print()

# List_Files()


def Download_File(file):
    List_Files()
    # file = 'Files/' + input('Enter File Name from above list : ')

    resp = requests.get(
        urljoin(api_base, f"files/path/home/{username}/mysite/input/{file}"),
        headers={"Authorization": "Token {api_token}".format(api_token=api_token)}
    )

    with open(f'{file}', 'wb') as f:
        f.write(resp.content)

# Download_File(file)


def Upload_File(file):
    # file = 'Files/' + input('Enter File Name : ')

    with open(f'{file}', 'rb') as f:
        cont = f.read()

    requests.post(
        urljoin(api_base, f"files/path/home/{username}/mysite/input/{file}"),
        files={"content": cont},
        headers={"Authorization": f"Token {api_token}"}
    )

# Upload_File(file)
