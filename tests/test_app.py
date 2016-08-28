import io

import pytest

import app as app_module


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(app_module, 'UPLOAD_FOLDER', tmp_path)
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as test_client:
        yield test_client


def upload(client, filename, content=b'fake-content'):
    return client.post(
        '/upload',
        data={'file': (io.BytesIO(content), filename)},
        content_type='multipart/form-data',
    )


def test_index_ok(client):
    response = client.get('/')
    assert response.status_code == 200


def test_upload_mp3(client, tmp_path):
    response = upload(client, 'song.mp3')
    assert response.status_code == 200
    assert (tmp_path / 'song.mp3').exists()


def test_upload_image(client, tmp_path):
    response = upload(client, 'photo.JPG')
    assert response.status_code == 200
    assert (tmp_path / 'photo.jpg').exists()


def test_upload_rejects_unsupported_type(client, tmp_path):
    response = upload(client, 'evil.sh')
    assert response.status_code == 400
    assert list(tmp_path.iterdir()) == []


def test_upload_rejects_missing_file(client):
    response = client.post('/upload', data={}, content_type='multipart/form-data')
    assert response.status_code == 400


def test_upload_sanitizes_path_traversal(client, tmp_path):
    response = upload(client, '../../etc/passwd.mp3')
    assert response.status_code == 200
    saved = list(tmp_path.iterdir())
    assert len(saved) == 1
    assert saved[0].parent == tmp_path
    assert '..' not in saved[0].name


def test_upload_chinese_filename_gets_random_name(client, tmp_path):
    response = upload(client, '音樂.mp3')
    assert response.status_code == 200
    saved = list(tmp_path.iterdir())
    assert len(saved) == 1
    assert saved[0].suffix == '.mp3'


def test_index_lists_uploaded_files(client, tmp_path):
    upload(client, 'song.mp3')
    upload(client, 'photo.png')
    response = client.get('/')
    html = response.get_data(as_text=True)
    assert 'song.mp3' in html
    assert 'photo.png' in html
