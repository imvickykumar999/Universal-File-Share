
from flask import Flask, url_for, render_template, request, redirect, session, flash, send_from_directory
from werkzeug.utils import secure_filename
from pathlib import Path
import sqlite3, os


conn = sqlite3.connect('test.db', 
            check_same_thread=False)

conn.execute('''
        CREATE TABLE IF NOT EXISTS ADMIN (
        USERNAME CHAR(50) PRIMARY KEY,
        PASSWORD CHAR(50) NOT NULL )
''')

app = Flask(__name__)
app.jinja_env.globals.update(os=os)


try:
    os.mkdir('static')
except:
    pass


@app.route('/', methods=['GET', 'POST'])
def home():    
    if request.method == 'POST':  
        f = request.files['file']

        filename = secure_filename(f.filename)
        saved = os.path.join('static', filename)
        f.save(saved)
    
    elif not session.get('logged_in'):
        return render_template('login.html')
    
    new_path = sorted(Path('static').iterdir(), key=os.path.getmtime)
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
                flash("Either Username or Password is wrong")
                return render_template('login.html')
            else:
                session['logged_in'] = True

                session['username'] = username.split("'")[0]
            return redirect(url_for('home'))
            
        except Exception as e:
            flash(f"{e}") 
            return redirect(url_for('home'))


# @app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']

        if username == '' or password == '':
            flash("Fill the empty field")
            return render_template('register.html')
        
        try:
            statement = f'''
                INSERT INTO ADMIN (USERNAME,PASSWORD) VALUES ('{username}', '{password}')
            '''
            conn.execute(statement)
            conn.commit()
            
        except:
            flash("Username already exists.")  
            return render_template('register.html')

        return render_template('login.html')
    return render_template('register.html')


@app.route("/logout/")
def logout():
    session['logged_in'] = False
    flash("You are successfuly Logged out") 
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.secret_key = "123"
    app.run(debug=True, 
            port=5000, 
            host='0.0.0.0',
            )
