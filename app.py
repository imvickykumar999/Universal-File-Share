
from flask import Flask, render_template, send_from_directory, request
from pathlib import Path
import os

app = Flask(__name__)
app.jinja_env.globals.update(os=os)

try:
    os.mkdir('input')
except:
    pass

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':  
        f = request.files['file']
        saved = os.path.join('input', f.filename)
        f.save(saved)  
    
    new_path = sorted(Path('./input').iterdir(),
                        key=os.path.getmtime)
    
    return render_template('index.html', 
                           new_path=new_path)

@app.route('/input/<filename>')
def send_vixtify(filename):
    return send_from_directory("input", filename)


if __name__ == '__main__':
    app.run(debug=True, 
            port=5000, 
            host='0.0.0.0',
            )
