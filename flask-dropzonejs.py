from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_PATH = 'static/uploads'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_PATH)


@app.route('/')
def index():
    all_image_files = []
    all_mp3_files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        ## 圖片檔
        if (isImageFormat(filename)):
            all_image_files.append(filename)
        ## mp3
        if (filename.find('.mp3') > -1):
            all_mp3_files.append(filename)
    return render_template('index.html', **locals());


# 符合圖片檔案
def isImageFormat(link):
    if (link.find('.jpg') > -1 or link.find('.png') > -1 or link.find('.gif') > -1 or link.find('.jpeg') > -1):
        return True;
    return False;


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        upload_path = '{}/{}'.format(UPLOAD_FOLDER, file.filename)
        file.save(upload_path)
        return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
