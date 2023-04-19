
# unzip /home/imvickykumar999/mysite/your_file.zip

from urllib.parse import urljoin
import requests, os


username = 'imvickykumar999'
pythonanywhere_host = "www.pythonanywhere.com"
api_base = f"https://{pythonanywhere_host}/api/v0/user/{username}/"


folder = ('vicks', '.')[1]
with open(f'{folder}/API_Token.txt', 'r') as f:
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
        urljoin(api_base, 
                f"files/path/home/{username}/mysite/static/"
                ),
        headers={"Authorization": f"Token {api_token}"}
    )

    print()
    enum = list(resp.json().keys())

    for i,j in enumerate(resp.json().keys()):
        print(i+1, '). ', j)

    print()
    return enum

# all_files = List_Files()
# print(all_files)


def Download_File(file):    
    resp = requests.get(
        urljoin(api_base, 
                f"files/path/home/{username}/mysite/static/{os.path.basename(file)}"
                ),
        headers={"Authorization": "Token {api_token}".format(api_token=api_token)}
    )

    with open(f'{file}', 'wb') as f:
        f.write(resp.content)

# List_Files()
# file = 'static/' + input('Enter File Name from above list to Download : ')
# Download_File(file)


def Upload_File(file):
    with open(f'{file}', 'rb') as f:
        cont = f.read()

    requests.post(
        urljoin(api_base, 
                f"files/path/home/{username}/mysite/static/{os.path.basename(file)}"
                ),
        files={"content": cont},
        headers={"Authorization": f"Token {api_token}"}
    )

# file = 'static/' + input('Enter File Name to Upload : ')
# Upload_File(file)


def Delete_File(file):
    requests.delete(
        urljoin(api_base, f"files/path/home/{username}/mysite/static/{os.path.basename(file)}"),
        headers={"Authorization": f"Token {api_token}"}
    )

# print('\n\t>>> Before Deletion ...')
# List_Files()
# file = input('Enter File Name from above list to Delete : ')

# print('\n\t>>> After Deletion ...')
# Delete_File(file)
# List_Files()
