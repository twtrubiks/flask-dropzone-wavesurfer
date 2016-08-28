import uuid
from pathlib import Path

from flask import Flask, abort, render_template, request
from werkzeug.utils import secure_filename

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / 'static' / 'uploads'

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif'}
AUDIO_EXTENSIONS = {'.mp3'}
ALLOWED_EXTENSIONS = IMAGE_EXTENSIONS | AUDIO_EXTENSIONS

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 單一請求上限 50 MB

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@app.route('/')
def index():
    files = sorted(path.name for path in UPLOAD_FOLDER.iterdir() if path.is_file())
    images = [name for name in files if Path(name).suffix.lower() in IMAGE_EXTENSIONS]
    audios = [name for name in files if Path(name).suffix.lower() in AUDIO_EXTENSIONS]
    return render_template('index.html', images=images, audios=audios)


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file is None or not file.filename:
        abort(400, '沒有收到檔案')

    suffix = Path(file.filename).suffix.lower()
    if suffix not in ALLOWED_EXTENSIONS:
        abort(400, '不支援的檔案格式')

    # secure_filename 會過濾路徑與特殊字元，純中文檔名會被濾成空字串，此時改用隨機檔名
    stem = secure_filename(Path(file.filename).stem) or uuid.uuid4().hex
    file.save(UPLOAD_FOLDER / f'{stem}{suffix}')
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
