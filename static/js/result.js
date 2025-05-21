// app.pyから受け取った（？）ヒット数をもとに表示数を決める。
// 1~10ヒットなら全て表示する。
// 11ヒット以上なら（可能なら）ランダムで10個のみ表示。もしくは前から10個表示。
// 各「car_info_数字」のidについてそれぞれ表示するか決めるif文を書く？

// ヒット数が1以下なら表示しない
// document.addEventListener('DOMContentLoaded', function() {
    hit_count=hitCount // 仮置きのヒット数。本来ならpythonかhtmlから受け取らないといけないが現在受け取れていない。

    if(hit_count <= 1){
        car_info_2=document.getElementById("car_info_2")
    car_info_2.style.display = "none";
    }
    if(hit_count <= 2){
        car_info_3=document.getElementById("car_info_3")
    car_info_3.style.display = "none";
    }
    if(hit_count <= 3){
        car_info_4=document.getElementById("car_info_4")
    car_info_4.style.display = "none";
    }
    if(hit_count <= 4){
        car_info_5=document.getElementById("car_info_5")
    car_info_5.style.display = "none";
    }
    if(hit_count <= 5){
        car_info_6=document.getElementById("car_info_6")
    car_info_6.style.display = "none";
    }
    if(hit_count <= 6){
        car_info_7=document.getElementById("car_info_7")
    car_info_7.style.display = "none";
    }
    if(hit_count <= 7){
        car_info_8=document.getElementById("car_info_8")
    car_info_8.style.display = "none";
    }
    if(hit_count <= 8){
        car_info_9=document.getElementById("car_info_9")
    car_info_9.style.display = "none";
    }
    if(hit_count <= 9){
        car_info_10=document.getElementById("car_info_10")
    car_info_10.style.display = "none";
    }
// });