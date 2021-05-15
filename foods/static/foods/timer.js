function timeToString(time) {
  let diffInHrs = time / 3600000;
  let hh = Math.floor(diffInHrs);

  let diffInMin = (diffInHrs - hh) * 60;
  let mm = Math.floor(diffInMin);

  let diffInSec = (diffInMin - mm) * 60;
  let ss = Math.floor(diffInSec);

  let diffInMs = (diffInSec - ss) * 100;
  let ms = Math.floor(diffInMs);

  let formattedMM = mm.toString().padStart(2, "0");
  let formattedSS = ss.toString().padStart(2, "0");
  let formattedMS = ms.toString().padStart(2, "0");

  return `${formattedMM}:${formattedSS}:${formattedMS}`;
}

let startTime;
let elapsedTime = 0;
let timerInterval;
let stopped = true;

function print(txt) {
    document.getElementById("timershow").innerHTML = txt;
}

function start() {
    stopped = false;
    startTime = Date.now();
    timerInterval = setInterval(function printTime() {
        if (stopped == true) {
            clearInterval(timerInterval);
            timerInterval = 0;
        } else {
            elapsedTime = Date.now() - startTime;
            print(timeToString(elapsedTime));
        }
    }, 10);
}

function pause() {
    stopped = true;
    document.getElementById('id_time').value() = timerInterval;
    clearInterval(timerInterval);
}

function reset() {
    stopped = true;
    document.getElementById('id_time').val() = timerInterval;
    clearInterval(timerInterval);
    print("00:00:00");
    elapsedTime = 0;
}

let playButton = document.getElementById("startTimer");
let pauseButton = document.getElementById("pauseTimer");
let resetButton = document.getElementById("resetTimer");

playButton.addEventListener("click", start);
pauseButton.addEventListener("click", pause);
resetButton.addEventListener("click", reset);

window.addEventListener("keydown", function(event) {
    if (stopped == true) {
        start();
    } else if (stopped == false) {
        pause();
    }
}, true);

//$(document).ready(function(){
//    $("#pauseTimer").click(function() {
//        $.ajax({
//            url: '',
//            type: 'get',
//            data: {
//                time: elapsedTime.text(),
//            },
//            success: function(response) {
//                $("#successp").text(response.seconds)
//            },
//        });
//    });
//});
