
import requests, zipfile, os
URL = 'https://github.com/imvickykumar999/Universal-File-Share/raw/main/vicks/shareit.zip'

r = requests.get(URL, allow_redirects=True)
open('android.zip', 'wb').write(r.content)

with zipfile.ZipFile('android.zip', 'r') as zip_ref:
    zip_ref.extractall('.')

print('''

Access this link from any Device nearby.

''')
os.system('python app.py')
