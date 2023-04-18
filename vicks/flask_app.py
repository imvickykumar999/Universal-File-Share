
from flask import Flask, render_template, send_from_directory, request
from vicks import upload_files as uff
import os

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

        file = os.path.join('static', f.filename)
        # f.save(file)
        uff.Upload_File(file)

    new_path = sorted(uff.List_Files())
    return render_template('index.html',
                           new_path=new_path)


@app.route('/static/<filename>')
def send_vixtify(filename):
    return send_from_directory("/home/imvickykumar999/mysite/static", filename)
    # return send_from_directory("static", filename)


if __name__ == '__main__':
    app.run(debug=True,
            port=5000,
            host='0.0.0.0',
            )
