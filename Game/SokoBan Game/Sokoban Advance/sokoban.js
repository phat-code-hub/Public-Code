"use strict";
var ctx,gc; // Canvas
const imgFol="https://raw.githubusercontent.com/phat-code-hub/CodeData/main/SokoBan/";
const imgList= {Wall: "Wall.png",
                "Goal": "Goal.png",
                "Luggage":"Luggage.png",
                "ManL": "ManL.png",
                "ManU":"ManU.png",
                "ManR":"ManR.png",
                "ManD":"ManD.png"
                }
//Worker starting position
var px,py; 
//direction of worker image
var direction =0
var step=0,steps; // count number of walked step
var goalNo=0,filled=0, filled_state; // check filling up all of goal 
// 1:Goal , 2:Luggage, 4: Clear (no color) block , 6:Wall
var data=[];
//Game data is optional depend on your decision , here are 3 games as examples
//Game 1 data : px =1 , py =1
var data1 =[
    [6,6,6,6,6,4,4],
    [6,0,0,0,6,4,4],
    [6,0,6,2,6,6,6],
    [6,0,2,0,1,1,6],
    [6,6,6,6,6,6,6]
]
//Game 2 data : px =12 , py =8
var data2=[
    [4,4,4,4,6,6,6,6,6,4,4,4,4,4,4,4,4,4,4],
    [4,4,4,4,6,0,0,0,6,4,4,4,4,4,4,4,4,4,4],
    [4,4,4,4,6,2,0,0,6,4,4,4,4,4,4,4,4,4,4],
    [4,4,6,6,6,0,0,2,6,6,6,4,4,4,4,4,4,4,4],
    [4,4,6,0,0,2,0,0,2,0,6,4,4,4,4,4,4,4,4],
    [6,6,6,0,6,0,6,6,6,0,6,4,4,6,6,6,6,6,6],
    [6,0,0,0,6,0,6,6,6,0,6,6,6,6,0,0,1,1,6],
    [6,0,2,0,0,2,0,0,0,0,0,0,0,0,0,0,1,1,6],
    [6,6,6,6,6,0,6,6,6,6,0,6,0,6,0,0,1,1,6],
    [4,4,4,4,6,0,0,0,0,0,0,6,6,6,6,6,6,6,6],
    [4,4,4,4,6,6,6,6,6,6,6,6,4,4,4,4,4,4,4]

]

//Game3 data : px =1 , py =1
var data3 =[
    [6,6,6,6,6,4,4,4,4],
    [6,0,0,0,6,4,4,4,4],
    [6,0,2,2,6,4,6,6,6],
    [6,0,2,0,6,4,6,1,6],
    [6,6,6,0,6,6,6,1,6],
    [4,6,6,0,0,0,0,1,6],
    [4,6,0,0,0,6,0,0,6],
    [4,6,0,0,0,6,0,0,6],
    [4,6,0,0,0,6,6,6,6],
    [4,6,6,6,6,6,4,4,4]
]
//Select Game
function select(GameNo){
    switch (GameNo){
        case 2:{
                data = data2;
                px=12,py=8;
                break;
            }
        case 3:{
                data = data3;
                px=1,py=1;
                break;
            }
        default:// Game 1
        {
            data = data1;
            px=1,py=1;
        }
    }   
    ctx.width = data[0].length*40;
    ctx.height=data.length*40;
}
//Take Goals Total
function goalTotal(){
    for (let y =0; y<data.length;y++){
        for (let x=0;x<data[y].length;x++ ){
            if (data[y][x] == 1) goalNo++;
        }
    }

}
//Init Image
function initImage(){
    for (const key in imgList){
        const img =document.getElementById(key);
        img.setAttribute("src",imgFol+imgList[key]);
    }
}
// 
//Init function
function init(){
    steps = document.getElementById("step");
    filled_state= document.getElementById("filled");
    ctx = document.getElementById("soko");
    gc= ctx.getContext("2d");
    // initImage();
    select(3);//select Game 3
    goalTotal();
    onkeydown =mykeydown;
    repaint();
}

// Keydown event handle
function mykeydown(e){
    var dx0 =px,dx1 =px,dy0=py,dy1=py;
    direction =e.keyCode % 37;
    switch(e.keyCode){
        case 37: //keyLeft
            {
                dx0--;dx1-=2;
                break;
            }
        case 38://keyUp
            {
                dy0--;dy1-=2;
                break;
            }
        case 39://KeyRight
        {
            dx0++;dx1+=2;
            break;
        }
        case 40://KeyDown
        {
            dy0++;dy1+=2;
            break;
        }
    }

    if((data[dy0][dx0] & 0x2) == 0){ //no wall , no Luggage -> move forward
        px = dx0;
        py = dy0;
        step++;
    } else if ((data[dy0][dx0] & 0x6)== 2) { // have a Luggage in front of moving direction ( first block)
        if((data[dy1][dx1] & 0x2) == 0) { // no wall , no Luggage at the second block -> move forward
            data[dy0][dx0] ^= 2; // clear Luggage in front  (first)
            data[dy1][dx1] |=2; // set Luggage at second blocks
            px =dx0;
            py =dy0;
            step++;
        }
    }
    repaint()
}
//Keypress recognize
function kUp(){
    mykeydown({keyCode:38});
}
function kDown(){
    mykeydown({keyCode:40});
}
function kLeft(){
    mykeydown({keyCode:37});
}
function kRight(){
    mykeydown({keyCode:39});
}
// Refresh Canvas
function repaint( ){
    gc.filStyle = "black";
    gc.fillRect (0,0,ctx.width,ctx.height);

    for(let y =0; y<data.length;y++){
        for (let x=0;x<data[y].length;x++ ){
            if(data[y][x] & 0x1){
                gc.drawImage(Goal,x*40,y*40,40,40);
            }
            // if(data[y][x] & 0x2){
            //     gc.drawImage(Luggage,x*40,y*40,40,40);
            // }
            if(data[y][x] == 4){
                gc.clearRect(x*40,y*40,40,40);
            }
            if(data[y][x] == 6){
                gc.drawImage(Wall,x*40,y*40,40,40);
            }
        }
    }
    switch(direction){
        case 0:{
            gc.drawImage(ManL,px*40,py*40,40,40);
            break;
        }
        case 1:{
            gc.drawImage(ManU,px*40,py*40,40,40);
            break;
        }
        case 2:{
            gc.drawImage(ManR,px*40,py*40,40,40);
            break;
        }
        case 3:{
            gc.drawImage(ManD,px*40,py*40,40,40);
            break;
        }
    }
    steps.innerHTML = step;
    filled_state.innerText = filled;
    check();
}
//Check all goals were filled up or not 
function check(){
    filled=0;
    for(let y =0; y<data.length;y++){
        for (let x=0;x<data[y].length;x++ ){
            if((data[y][x] & 0x1) && (data[y][x] & 0x2)){
                    filled++;
            }
        }
    }
    if (filled == goalNo) alert("Congratulation!");
}   
function Undo(){
    // gc.clearRect(px*40,py*40,40,40);
    // gc.filStyle = "black";
    // gc.fillRect (px*40,py*40,40,40);
    // gc.drawImage(Goal,px*40,py*40,40,40);
    initImage();
}