$(document).ready(function () {
    $(".fa-play-circle").click(function () {
        $(this).toggleClass("fa-pause-circle");
    });
    $(".fa-stop-circle").click(function () {
        $(this).parent().find("i.fa-play-circle").removeClass("fa-pause-circle");
    });

});