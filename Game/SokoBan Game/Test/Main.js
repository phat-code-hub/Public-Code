"use strict";
function getData(level,stage){
    // let data0=extractData(level,Data);
    // return data0;
    return [1,1,"6666644-6000644-6062666"+
                "-6020116-6666666"];
}
function init(){
    ctx = document.getElementById("canvas");
    gc =ctx.getContext("2d");
    initImage();
    curLevel=1;//EASY
    curStage=1;//Scence 1
}
//Main Function
function Play(){
    [px,py,curData]=getData(curLevel,curStage);
    direction =-3;// ManL image
    isPushed =false;
    isUndo=false;
    histCount=0;
    curCord =new Cord(px,py,direction);//worker starting  Cord
    curLugCord= new Cord(px,py,direction);//Luggage starting Cord
    Begin();
}
// Start Game
function Begin(){
    //Extract data info
    data0=[],data=[];
    let img_datas= curData.split('-');
    img_datas.forEach(el=>{
        data0.push(el.split(""));
        data.push(el.split(""));
    } )
    //draw Canvas
    ctx.width = data0[0].length*CELL;
    ctx.height=data0.length*CELL;
    drawCanvas();
    //put worker image
    gc.drawImage(images[direction],px*CELL,py*CELL,CELL,CELL);
}
function saveHistory(){
    let tmpD=[];
    let tmpHist=[];
    let tmpC ;
    if(Array.isArray(data)){
         data.forEach(el =>{
                        el.forEach(ml=>{
                        tmpD.push(ml);
                    })
                tmpHist.push(tmpD);
                tmpD=[];
                })
        tmpC= new Cord(curCord.x,curCord.y,curCord.dir);
        hist.push(new History(tmpHist,tmpC));
        histCount++;
    }
    
}
// Keydown event handle
function mykeydown(e){
    saveHistory();
    dx0 =px,dx1 =px,dy0=py,dy1=py;
    curCord.x=px, curCord.y=py;
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
    } 
    else if ((data[dy0][dx0] & 0x6)== 2) { // have a Luggage in front of moving direction ( first block)
        if((data[dy1][dx1] & 0x2) == 0) { // no wall , no Luggage at the second block -> move forward
            data[dy0][dx0] ^= 0x2; // clear Luggage in front  (first)
            data[dy1][dx1] |=0x2; // set Luggage at second blocks
            px =dx0;
            py =dy0;
            curLugCord.x=dx1;
            curLugCord.y=dy1;
            step++;
            isPushed=true;
        }
        
    }
    direction = direct_arr[e.keyCode];
    curLugCord.dir=direction;
    curCord.dir =direction;
    UpdateScence();
}
//Keypress recognize
function kUp(){
    isPushed=false;
    mykeydown({keyCode:38});
}
function kDown(){
    isPushed=false;
    mykeydown({keyCode:40});
}
function kLeft(){
    isPushed=false;
    mykeydown({keyCode:37});
}
function kRight(){
    isPushed=false;
    mykeydown({keyCode:39});
}
function initImage(){
    for (const key in imgList){
        const img =document.createElement("img");
        img.src = imgFol+imgList[key][1];
        img.id =key;
        img.alt=key;
        img.style.display="none";
        img.crossOrigin = "Anonymous";
        ctx.appendChild(img)
        images[parseInt(imgList[key][0])] =img;
    }
}
function Choice(num){
    curLevel=num;
}

function extractData(l,d){
    
}

function drawCanvas(){
    gc.clearRect(0,0,ctx.width,ctx.height);
    gc.fillStyle ="black";
    gc.fillRect(0,0,ctx.width,ctx.height);
    // put images on canvas
    for (let y= 0;y<data.length;y++){
        for(let x=0;x<data[y].length;x++){
            if(data[y][x] & 0x1){
                gc.drawImage(images[1],x*CELL,y*CELL,CELL,CELL);
            }
            if(data[y][x] & 0x2){
                gc.drawImage(images[2],x*CELL,y*CELL,CELL,CELL);
            }
            if(data[y][x] == 4){
                gc.clearRect(x*CELL,y*CELL,CELL,CELL);
            }
            if(data[y][x] == 6){
                gc.drawImage(images[6],x*CELL,y*CELL,CELL,CELL);
            }
        }
    }
}
//Update scence after each moving
function UpdateScence(){
    //Clear unused previous images
    gc.clearRect(curCord.x*CELL,curCord.y*CELL,CELL,CELL);
    if(isPushed){
        gc.clearRect(curLugCord.x*CELL,curLugCord.y*CELL,CELL,CELL);
    } 
    gc.fillStyle ="black";
    gc.fillRect(curCord.x*CELL,curCord.y*CELL,CELL,CELL);
    if (data[curCord.y][curCord.x] & 0x1) {// Prev Position is Goal
            gc.drawImage(images[1],curCord.x*CELL,curCord.y*CELL,CELL,CELL);
    }
    // Push Luggage
    if (isPushed) gc.drawImage(images[2],curLugCord.x*CELL,curLugCord.y*CELL,CELL,CELL);
    //Draw new worker image
    let UndoFlag = isUndo?-1:1;
    gc.drawImage(images[UndoFlag*direction],px*CELL,py*CELL,CELL,CELL);
    isUndo=false;
    curCord.x=px,curCord.y=py;
}
function Undo(){
    if(hist.length>0) {
        isUndo=true;
        let tmpData = hist.pop();
        // popHistD= tmpData.data;
        // popHistC=tmpData.Cord;
        data = tmpData.data;
        curCord =tmpData.Cord;
        direction = tmpData.Cord.dir;
    };
    drawCanvas();
    gc.drawImage(images[direction],curCord.x*CELL,curCord.y*CELL,CELL,CELL);
}