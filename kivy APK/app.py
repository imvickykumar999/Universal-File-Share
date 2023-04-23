
from flask import Flask, url_for, render_template, request, redirect, session, send_from_directory
from werkzeug.utils import secure_filename
import sqlite3, os, requests
from pathlib import Path
import numpy as np

try:
    os.mkdir('static')
except:
    pass

conn = sqlite3.connect('test.db', 
            check_same_thread=False)

conn.execute('''
        CREATE TABLE IF NOT EXISTS ADMIN (
        USERNAME CHAR(50) PRIMARY KEY,
        PASSWORD CHAR(50) NOT NULL )
''')

app = Flask(__name__)
app.jinja_env.globals.update(
                             session=session,
                             sorted=sorted,
                             int=int,
                             os=os,
                             np=np,
                             )


def extract_frames(static_username, filename):
    import cv2

    saved = os.path.join(static_username, filename)
    vidcap = cv2.VideoCapture(saved)
    success, image = vidcap.read()

    filename = filename.split('.')[0]
    folder = os.path.join(static_username, filename)

    try:
        os.mkdir(folder)
    except Exception as e:
        print(e)

    count = 0
    while success:
        cv2.imwrite(f"{folder}/{count}.jpg", image)     # save frame as JPEG file      
        success,image = vidcap.read()
        # print('Read a new frame: ', success)
        count += 1


def getname(url):
    url = list(url.split('/'))

    if len(url) == 1:
        url = url[0]
        itis = 'user'

        if len(url) == 11 and url[0] == 'C':
            itis = 'reels'
    else:
        if url[3] in ['reels', 'reel', 'p']:
            url = url[4]
            itis = 'reels'
        else:
            url = url[3]
            itis = 'user'

    return url, itis


@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        static_username = 'static/' + session['username']
    except:
        static_username = 'static'

    try:
        reqid = getname(request.args.get("URL"))[0]
        link = f'https://www.instagram.com/p/{reqid}/?__a=1&__d=1'

        fetch = requests.get(link).json()['graphql']
        return redirect(fetch['shortcode_media']['video_url'], 
                        code=200)
    except:
        pass

    try:
        os.mkdir(static_username)
    except:
        pass

    if request.method == 'POST':  
        f = request.files['file']

        filename = secure_filename(f.filename)
        saved = os.path.join(static_username, filename)
        f.save(saved)

        checkbox = len(request.form.getlist('checked'))
        checkfile = filename.split('.')[-1].lower() in ['mp4', 'avi']

        if checkfile and checkbox:
            try:
                extract_frames(static_username, filename)
            except Exception as e:
                print(e)
    
    elif not session.get('logged_in'):
        return render_template('login.html')
    
    new_path = sorted(Path(static_username).iterdir(), key=os.path.getmtime)
    return render_template('index.html', new_path=new_path)


@app.route('/static/<filename>')
def send_vixtify(filename):
    return send_from_directory("static", filename)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']

        try:
            statement = f'''
                SELECT * FROM ADMIN WHERE USERNAME='{username}' AND PASSWORD='{password}'
            '''
            crsr = conn.execute(statement)
            # print(statement, username.split("'")[0])

            if crsr.fetchone() is None:
                return render_template('login.html')
            else:
                session['logged_in'] = True

                session['username'] = username.split("'")[0]
            return redirect(url_for('home'))
            
        except Exception as e:
            return redirect(url_for('home'))


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']

        if username == '' or password == '':
            return render_template('register.html')
        
        try:
            statement = f'''
                INSERT INTO ADMIN (USERNAME,PASSWORD) VALUES ('{username}', '{password}')
            '''
            conn.execute(statement)
            conn.commit()
            
        except:
            return render_template('register.html')

        return render_template('login.html')
    return render_template('register.html')


@app.route("/logout/")
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.secret_key = "123"
    app.run(debug=True, 
            port=5000, 
            host='0.0.0.0',
            )
