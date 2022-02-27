"use strict";
//Data Group : define many canvas by level and scence depend your option : 
// DataSource=[
//         //Easy
//         ["11,20,",
//          []
//         ],
//         //Middle
//         [

//         ],
//         //Hard
//         [

//         ]
// ];





var gc;
var px=12,py=8; // Worker Start Position
var level = 0, grad =0;
var direction =0
// 1:Goal , 2:Luggage, 4: Clear (no color) block , 6:Wall
var data;
data =[
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
//Choice play scence
function setScence (l,n){
    // data = DataSource[l][n];
}
//Init function
function init(){
    // setScence(level,grad);
    gc = document.getElementById("soko").getContext("2d");
    onkeydown =mykeydown;
    repaint(5);
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
    } else if ((data[dy0][dx0] & 0x6)== 2) { // have a Luggage in front of moving direction ( first block)
        if((data[dy1][dx1] & 0x2) == 0) { // no wall , no Luggage at the second block -> move forward
            data[dy0][dx0] ^= 2; // clear Luggage in front  (first)
            data[dy1][dx1] |=2; // set Luggage at second blocks
            px =dx0;
            py =dy0;
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
    gc.fillRect (0,0,760,440);

    for(let y =0; y<data.length;y++){
        for (let x=0;x<data[y].length;x++ ){
            if(data[y][x] & 0x1){
                gc.drawImage(Goal,x*40,y*40,40,40);
            }
            if(data[y][x] & 0x2){
                gc.drawImage(Luggage,x*40,y*40,40,40);
            }
            if(data[y][x] == 4){
                gc.clearRect(x*40,y*40,40,40);
            }
            if(data[y][x] == 6){
                gc.drawImage(Wall,x*40,y*40,40,40);
            }
        }
    }
    // gc.drawImage(ManR,px*40,py*40,40,40);
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
    
}