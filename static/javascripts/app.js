document.addEventListener('DOMContentLoaded', function () {
    FilePond.create(document.querySelector('.filepond'), {
        name: 'file',
        allowMultiple: true,
        server: { process: '/upload' },
        labelIdle: '拖曳檔案到這裡，或 <span class="filepond--label-action">點擊選擇</span>（jpg / jpeg / png / gif / mp3）'
    }).on('processfiles', function () {
        // 全部檔案上傳完成後重新整理，讓新檔案直接顯示在頁面上
        window.location.reload();
    });

    document.querySelectorAll('.player').forEach(function (player) {
        var wavesurfer = WaveSurfer.create({
            container: player.querySelector('.waveform'),
            waveColor: 'violet',
            progressColor: 'purple',
            url: player.dataset.src
        });
        var playIcon = player.querySelector('.icon-play');
        var pauseIcon = player.querySelector('.icon-pause');

        player.querySelector('.btn-play').addEventListener('click', function () {
            wavesurfer.playPause();
        });
        player.querySelector('.btn-stop').addEventListener('click', function () {
            wavesurfer.stop();
        });
        wavesurfer.on('play', function () {
            playIcon.hidden = true;
            pauseIcon.hidden = false;
        });
        wavesurfer.on('pause', function () {
            playIcon.hidden = false;
            pauseIcon.hidden = true;
        });
    });
});
