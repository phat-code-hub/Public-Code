"use strict";
// Global Variable
var ctx,tiles =[],moves=[],mIndex=0,mCount=0,times=[];
var timer = NaN,startTime=NaN,elapsed=0,score=0,bgimage,sound;
var mouseX = null,mouseY=null,mouseUpX=null,mouseUpY=null;
var message =["","good","very good","super","wonderful!",
                "great!!","amazing","brilliant!","excellent!!"];

// Define Tile Object
function Tile(x,y){
    this.x  = x;
    this.y  = y;
    this.px = x;
    this.py = y;
    this.count = 0;
    this.getX =function(){
        return this.x +(this.px-this.x)*(this.count)/20;
    };
    this.getY = function(){
        return this.y+(this.py-this.y)*(this.count)/20;
    };
    this.move = function(px,py,color){
        this.px = px;
        this.py =py;
        this.color = color;
        this.count = 20;
        this.moving = true;
        moves.push(this)
    };
    this.update = function(){
        if(--this.count <= 0){
            this.moving = false;
        }
    }
}
// Procedures
function rand(v){
    return Math.floor(Math.random()*v);
}
function iterate(f){
    for(let x=0;x<12;x++){
        for(let y=0;y<12;y++){
            f(x,y,tiles[x][y]);
        }
    }
}
// Main Code
function init(){
    for (var x=0;x<12;x++){
        tiles[x] = [];
        for(var y=0;y<12;y++){
            tiles[x][y] = new Tile(x,y);
        }
    }
    // Distribute starting color without 3 consecutive color blocks
    iterate (function(x,y,t){
        while(true){
            var r= rand(5);
            if (setColor(x,y,r)){
                t.color =r;
                break;
            }
        }
    });
    // Init remain time
    for (let i=0;i<15;i++){
        var t = document.createElement("img");
        t.src = "time"+i+".png";
        times.push(t);
    }
    //Init Canvas
    bgimage = document.getElementById("bgimage");
    var canvas = document.getElementById("canvas");
    ctx = canvas.getContext("2d");
    ctx.textAlign ="center";

    // sound =  document.getElementById("sound");
    repaint();
}


//Start event function
function go(){
    var canvas = document.getElementById("canvas");
    // Event handle
    canvas.onmousedown = mymousedown; 
    canvas.onmouseup = mymouseup;
    // append touch mode event handle
    canvas.addEventListener('touchstart',mymousedown);
    canvas.addEventListener('touchmove',mymousemove);
    canvas.addEventListener('touchend',mymouseup);
    //
    startTime = new Date();
    timer = setInterval(tick,25);

    document.body.addEventListener("touchmove",function(e){
        e.preventDefault();},
        false);
    document.getElementById("start").style.display="none";
    // document.getElementById("bgm").play();
}
// SetColor Function
function setColor(x,y,c){
    var flag = true;
    if (1<x) { // Left
        var c0 = tiles[x-2][y].color;
        var c1 = tiles[x-1][y].color;
        flag &= !(c0 == c1 && c1 == c);
    }
    if (x < 8) { // Right
        var c0 = tiles[x+2][y].color;
        var c1 = tiles[x+1][y].color;
        flag &= !(c0 == c1 && c1 == c);
    }
    if (1<y) { // Top
        var c0 = tiles[x][y-2].color;
        var c1 = tiles[x][y-1].color;
        flag &= !(c0 == c1 && c1 == c);
    }
    if (y < 8) { // Down
        var c0 = tiles[x][y+2].color;
        var c1 = tiles[x][y+1].color;
        flag &= !(c0 == c1 && c1 == c);
    }
    return flag;
}
//Canvas Event Handle
function mymousedown(e){
    mouseX = !isNaN(e.offsetX)? e.offsetX:e.touches[0].clientX;
    mouseY = !isNaN(e.offsetY)? e.offsetY:e.touches[0].clientY; 
}
function mymousemove(e){
    mouseUpX = !isNaN(e.offsetX)? e.offsetX:e.touches[0].clientX;
    mouseUpY = !isNaN(e.offsetY)? e.offsetY:e.touches[0].clientY; 
}
function mymouseup(e){
    var sx = Math.floor((mouseX-34)/44);
    var sy = Math.floor((mouseY-36)/44);
    var nx = sx , ny = sy;
    var mx = !isNaN(e.offsetX)? e.offsetX:mouseUpX;
    var my = !isNaN(e.offsetY)? e.offsetY:mouseUpY;
    if(Math.abs(mx-mouseX)>Math.abs(my-mouseY)){
        nx += (mx-mouseX>0)?1:-1;
    } else {
        ny +=(my-mouseY>0)?1:-1;
    }

    if(nx>11||ny>11||nx<0||ny<0||
        tiles[sx][sy].moving||tiles[nx][ny].moving){
            return;
        }
    
    var c = tiles[sx][sy].color;
    tiles[sx][sy].move(nx,ny,tiles[nx][ny].color);
    tiles[nx][ny].move(sx,sy,c);
    repaint();
}

//Main loop tick function
function tick(){
    //Fadeout effect of message
    mCount = Math.max(0,mCount-1);
    if (mCount == 0) {
        mIndex = 0;
    }
    if (moves.length >0) {
        for(let i =0;i<moves.length;i++){ // move tile
            moves[i].update();
        }
    }
    moves = moves.filter(function(t) {return t.count != 0});
    if (moves.length == 0) { // finish moving
        var s = removeTile(); //delete tile
        if (s >0 ){
            //Fisrt Time or Chain
            mIndex = Math.min(message.length-1,mIndex+1);
            mCount = 50;
            score += s*10 + mIndex*s *100;
            // sound.pause();
            // sound.currentTime = 0;
            // sound.play();
        }
        fall();
    }
    elapsed = ((new Date()).getTime()-startTime)/1000;
    if(elapsed>69) {
        clearInterval(timer);
        timer = NaN;
    }
    repaint();
}
//remove tiles when these tiles lined from 3 blocks  horizontal or vertical consecutively
//then set remove flag
function removeTile(){
    for (let y =0;y<12;y++){
        var c0 = tiles[0][y].color;
        var count =1;
        for (let x=1;x<12;x++){ // Horizontal Direction
            var c1 = tiles[x][y].color;
            if(c0 != c1) {
                c0 = c1;
                count =1;
            } else {
                if(++count >=3){
                    tiles[x-2][y].remove =true;
                    tiles[x-1][y].remove =true;
                    tiles[x-0][y].remove =true;
                }
            }
        }
    }
    for(let x=0;x<12;x++){ //Vertical Direction
        var c0 = tiles[x][0].color;
        var count = 1;
        for (let y=1;y<12;y++){
            var c1 = tiles[x][y].color;
            if(c0 != c1) {
                c0 = c1;
                c0 =c1;
                count =1;
            } else {
                if(++count >=3){
                    tiles[x][y-2].remove =true;
                    tiles[x][y-1].remove =true;
                    tiles[x][y-0].remove =true;
                }
            }
        }
    }
    var score = 0;
    iterate(function(x,y,t) {
        if(t.remove) {score++}; 
    });
    return score;
}
//fall handle function
function fall(){
    for (let x=0;x<12;x++){
        for(let y=11,sp=11;y>=0;y--,sp--){
            while (sp >=0) {
                if(tiles[x][sp].remove){
                    sp--;
                }else {
                    break;
                }
            }
            if(y !=sp) {
                var c =(sp>=0)? tiles[x][sp].color:rand(5);
                tiles[x][y].move(x,sp,c);
            }
        }
    }
    iterate(function(x,y,t){t.remove = false});
}

//Repaint
function repaint(){
    ctx.drawImage(bgimage,0,0);
    //Tile
    var images =[block0,block1,block2,block3,block4];
    iterate(function(x,y,t) {
        if(!t.remove) {
            ctx.drawImage(images[t.color],t.getX()*44+34,t.getY()*44+36,42,42);
        }
    });
    //Message
    ctx.font ="bold 80px sans-serif";
    ctx.fillStyle = "rgba(255,255,255, "+ (mCount/50)+")";
    ctx.fillText(message[mIndex],300,300);
    ctx.fillStyle="White";

    if (isNaN(timer)){
        ctx.fillText("FINISH",350,300);
    }

    //Score
    ctx.fillStyle ="rgba(220,133,30,50)";
    ctx.font ="bold 50px sans-serif";
    ctx.fillText(('0000000'+score).slice(-7),680,170);

    //Remain time
    var index = Math.min(15,Math.floor(elapsed/(69/15)));
    if (!isNaN(timer)){
        ctx.drawImage(times[index],615,327);
    }
    
}

