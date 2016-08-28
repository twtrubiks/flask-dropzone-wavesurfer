# flask-dropzone-wavesurfer
flask-dropzone-wavesurfer 使用Python Flask 搭配 Dropzone.js 和 WaveSurfer.js 
* [Demo](https://youtu.be/xPxZJBzia1Y)  
 
使用Python [Flask](http://flask.pocoo.org/) 搭配 [Dropzone.js](http://www.dropzonejs.com/) (可拖曳檔案上傳) 以及 [WaveSurfer.js](https://wavesurfer-js.org/) (播放音樂)的簡單範例程式，希望大家會喜歡:smile:

## 特色
* 透過 [Dropzone.js](http://www.dropzonejs.com/) (可拖曳檔案上傳) 。
* 透過 [WaveSurfer.js](https://wavesurfer-js.org/) (播放音樂)。
* 使用Python [Flask](http://flask.pocoo.org/)，輕鬆、簡單、快速。

## 執行說明
請先確定電腦有安裝 [Python](https://www.python.org/)

使用下列指令安裝套件
``` 
pip install -r requirements.txt
```

接著使用下列指令即可運行
``` 
python flask-dropzonejs.py
```

如下圖
<br>
![alt tag](http://i.imgur.com/oKK2JMX.jpg)

接著用你的瀏覽器瀏覽 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 執行畫面
[http://127.0.0.1:5000/](http://127.0.0.1:5000/) 為首頁 ，首頁畫面很簡單
![alt tag](http://i.imgur.com/lyHdk5g.jpg)
<br>
可拖曳想要上傳的音樂檔(mp3)以及圖片檔(.jpg .png .gif .jpeg)
<br>
![alt tag](http://i.imgur.com/A0ZH1hB.jpg)
檔案上傳完畢
<br>
![alt tag](http://i.imgur.com/IRwxx1a.jpg)
接著可以重新整理網頁(F5)，剛剛的資料會顯示在網頁上
![alt tag](http://i.imgur.com/oXv1ilB.jpg)
上傳的檔案會被保存在以下路徑
<b>flask-dropzone-wavesurfer\static\uploads </b>
<br><br>
音樂也是可以播放的哦，點播放的小圖示即可。
<br>
![alt tag](http://i.imgur.com/Rg1o0Jr.jpg)

## External JS
* [Dropzone.js](http://www.dropzonejs.com/) 
* [WaveSurfer.js](https://wavesurfer-js.org/) 
* [Font Awesome](http://fontawesome.io/) 

## 執行環境
* Python 3.5.2

## License
MIT license
