console.log("Hello world")

// initalize variables
let songIndex = 0;
let audioElement = new Audio('songs/music.mp3');
let masterPlay = document.getElementById('masterPlay');
let myProgressBar = document.getElementById('myProgressBar')
let playing = document.getElementById('playing');

let songItem = Array.from(document.getElementsByClassName('songItem'));

let songs = [
    {songName: "Susume" , filePath: "song/music.mp3"},
    {songName: "The real slim shady" , filePath: "song/eminem.mp3"},
    {songName: "Susume fuvaenu" , filePath: "song/music.mp3"},
    {songName: "The real slim shady ulnfc   auoi" , filePath: "song/eminem.mp3"},
    {songName: "Susume icfaeoiv" , filePath: "song/music.mp3"},
    {songName: "The real slim shady  aenfcauonfv" , filePath: "song/eminem.mp3"},
]


// console.log("Music playing")
// audioElement.play()
// handle play pause
masterPlay.addEventListener('click',()=>{
    if( audioElement.paused || audioElement.currentTime <=0){
        audioElement.play();
        masterPlay.classList.remove('fa-play-circle');
        masterPlay.classList.add('fa-pause-circle');
        playing.style.opacity=1;
    }
    else{
        audioElement.pause();
        masterPlay.classList.remove('fa-pause-circle');
        masterPlay.classList.add('fa-play-circle');
        playing.style.opacity=0; 
    }
})  





audioElement.addEventListener('timeupdate', ()=>{
    // console.log("time update");

    progress = parseInt((audioElement.currentTime/audioElement.duration)*100);
    // console.log(progress)
    myProgressBar.value = progress;

})



myProgressBar.addEventListener('change',()=>{
    audioElement.currentTime = myProgressBar.value*audioElement.duration/100;
})



songItem