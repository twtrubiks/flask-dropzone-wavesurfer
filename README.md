# flask-dropzone-wavesurfer

使用 Python [Flask](https://flask.palletsprojects.com/) 搭配 [FilePond](https://pqina.nl/filepond/)（可拖曳檔案上傳）以及 [WaveSurfer.js](https://wavesurfer.xyz/)（音波播放）的簡單範例程式，希望大家會喜歡 :smile:

* [Demo](https://youtu.be/xPxZJBzia1Y)（影片為舊版 Dropzone.js 介面，操作流程相同）

> 2026-06 更新：原本使用的 [Dropzone.js](https://www.dropzonejs.com/) 已停止維護，
> 上傳套件改用活躍維護中的 [FilePond](https://pqina.nl/filepond/)，

## 特色

* 透過 [FilePond](https://pqina.nl/filepond/) 拖曳上傳圖片（jpg / jpeg / png / gif）與音樂（mp3），上傳完成後自動重新整理列表。
* 透過 [WaveSurfer.js](https://wavesurfer.xyz/) v7 顯示音波並播放音樂。
* 使用 Python [Flask](https://flask.palletsprojects.com/)，輕鬆、簡單、快速。
* 伺服器端副檔名白名單 + `secure_filename` 檔名消毒，防止路徑穿越攻擊。
* 內建 pytest 測試。

## 執行說明

請先確定電腦有安裝 [Python](https://www.python.org/) 3.13+

使用下列指令安裝套件

```
pip install -r requirements.txt
```

接著使用下列指令即可運行

```
python app.py
```

接著用你的瀏覽器瀏覽 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 執行畫面

![alt tag](https://cdn.imgpile.com/f/Omd1OHu_xl.png)

可直接拖曳（或點擊選擇）想要上傳的音樂檔（mp3）以及圖片檔（jpg / png / gif / jpeg），全部檔案上傳完成後頁面會自動重新整理，剛上傳的資料就會顯示在網頁上。

上傳的檔案會被保存在以下路徑
<b>flask-dropzone-wavesurfer/static/uploads</b>（此資料夾不會進版控，啟動時自動建立）

音樂也是可以播放的哦，點波形上方的播放鈕即可，播放中會切換成暫停圖示，也可以按停止鈕回到開頭。

## 測試

```
pip install -r requirements-dev.txt
python -m pytest
```

## 專案結構

```
├── app.py                  # Flask 主程式（首頁列表 + 上傳 API）
├── requirements.txt        # 執行相依（Flask）
├── requirements-dev.txt    # 開發相依（pytest）
├── templates/index.html
├── static/
│   ├── javascripts/        # filepond / wavesurfer / app.js
│   ├── stylesheets/
│   └── uploads/            # 上傳的檔案（不進版控）
└── tests/test_app.py
```

## External JS

* [FilePond](https://pqina.nl/filepond/) 4.32.12
* [WaveSurfer.js](https://wavesurfer.xyz/) 7.12.7

## 執行環境

* Python 3.13.13

## License

MIT license
