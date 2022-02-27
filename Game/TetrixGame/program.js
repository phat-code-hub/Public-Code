//Define 7 Block shapes with 4 rotate states for each
block =[
    [
            //Block 0
        [
            [0,0,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [0,0,0,0]
        ],
        [
            [0,1,0,0],
            [0,1,1,0],
            [0,1,0,0],
            [0,0,0,0]
        ],
        [
            [0,1,0,0],
            [1,1,1,0],
            [0,0,0,0],
            [0,0,0,0]
        ],
        [
            [0,1,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,0,0,0]
        ]
    ],
    [
        //Block 1
        [
            [0,0,0,0],
            [1,1,1,0],
            [1,0,0,0],
            [0,0,0,0]
        ],
        [
            [1,0,0,0],
            [1,0,0,0],
            [1,1,0,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [0,0,1,0],
            [1,1,1,0],
            [0,0,0,0]
        ],
        [
            [1,1,0,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,0,0,0]
        ]
    ],
    [
       //Block 2
        [
            [0,0,0,0],
            [1,1,0,0],
            [0,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,1,0,0],
            [1,1,0,0],
            [1,0,0,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [1,1,0,0],
            [0,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,1,0,0],
            [1,1,0,0],
            [1,0,0,0],
            [0,0,0,0]
        ] 
    ],
    [
        //Block 3
        [
            [0,0,0,0],
            [0,1,1,0],
            [1,1,0,0],
            [0,0,0,0]
        ],
        [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [0,1,1,0],
            [1,1,0,0],
            [0,0,0,0]
        ],
        [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,0,0,0]
        ] 
    ],
    [
        //Block 4
        [
            [0,0,0,0],
            [1,1,1,0],
            [0,0,1,0],
            [0,0,0,0]
        ],
        [
            [1,1,0,0],
            [1,0,0,0],
            [1,0,0,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [1,0,0,0],
            [1,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,1,0,0],
            [0,1,0,0],
            [1,1,0,0],
            [0,0,0,0]
        ]
    ],
    [
        //Block 5
        [
            [0,0,0,0],
            [1,1,1,1],
            [0,0,0,0],
            [0,0,0,0]
        ],
        [
            [0,0,1,0],
            [0,0,1,0],
            [0,0,1,0],
            [0,0,1,0]
        ],
        [
            [0,0,0,0],
            [1,1,1,1],
            [0,0,0,0],
            [0,0,0,0]
        ],
        [
            [0,0,1,0],
            [0,0,1,0],
            [0,0,1,0],
            [0,0,1,0]
        ]
    ],
    [
        //Block 6
        [
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ],
        [
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ]
    ]
];
//Block Color
bColor=['#CC00CC','#FFA500','#CC0000',
        '#00CC00','#CC0000','#00CCCC','#CCCC00']
//array[22,12] to check collise, hit or not
state=[];
//--------------------------------------------
idirection=0; // Rotate Direction
ikind=0; // type of block index
cb=null; // game canvas
ct=null; // next block canvas 
ix=0,iy=0; // coordinate
bnext=0; // next block shape index
//--------------------------------------------
//On Window Load
//--------------------------------------------
function init(){
    backgamen=document.getElementById("back");
    cb=backgamen.getContext("2d");
    cb.fillStyle="#CCCCCC";
    cb.strokeStyle="#333333";
    cb.lineWidth=3;
    cb.fillRect(0,0,20,20);
    cb.strokeRect(0,0,20,20);
    // Draw left wall
    drawWall(0,0,22,0,20);
    //Draw right wall
    drawWall(220,0,22,0,20);
    //Draw bottom wall
    drawWall(0,420,22,20,0);

}
//--------------------------------------------
//Draw main wall of the window
function drawWall(x,y,iMax,xStep=0,yStep=0) {
    for (i=0;i<iMax;i++){
        cb.fillRect(x,y,20,20);
        cb.strokeRect(x,y,20,20);
        x+=xStep;
        y+=yStep;
    }
};
//--------------------------------------------
//Timer for Game
function timeMovement(){
    if(isContinue) {
        dropDown() ; // drop block automatically after each 1s
        //set next timer
        setTimeout(timeMovement,times);
    }
}
//--------------------------------------------
//When click GAME START button
//--------------------------------------------
function gamestart(){
    gamegamen=document.getElementById("game");
    cg=gamegamen.getContext("2d");
    // Clear canvas
    cg.clearRect(0,0,239,439);
    //Add score
    score =0;
    //set Timer info
    isContinue=true;
    times=1000;
    setTimeout(timeMovement,times);
    //Init or reset hit check array [22,12]
    //The walls are set to 99, safety (vacant) area :100, occupied area : block array index 
    state=new Array(22);
    for (i=0;i<22;i++){
        state[i]=new Array(12);
        for (j=0;j<12;j++){
            if (i==21) {
                state[21][j]=99
            } else {
                state[i][j]=100; 
            }
        }
        state[i][0]=99;
        state[i][11]=99
    }
    //Initial  random block
    ix=4;
    iy=0;
    idirection=Math.floor(Math.random()*3);
    ikind=Math.floor(Math.random()*7);
    draw(cg,ix,iy,idirection,ikind);
    //Show and set next shape block
    nextShape();
}
//--------------------------------------------
//Show next block
//--------------------------------------------
function nextShape(){
    bnext=Math.floor(Math.random()*7);
    nextGanmen=document.getElementById("next");
    ct=nextGanmen.getContext("2d");
    ct.clearRect(0,0,79,79);
    draw(ct,0,0,0,bnext);
}
//--------------------------------------------
//Draw shape by filling color at '1' cell of block array
//--------------------------------------------
function draw(c,bx,by,dir,kind){
    c.fillStyle=bColor[kind];
    c.strokeStyle="#333333";
    c.lineWidth=3;
    //choice shape by block kind and direction
    p=block[kind][dir];
    for (n=0;n<4;n++){
        for (m=0;m<4;m++){
            if (p[n][m] == 1) {
                c.fillRect((bx+m)*20,(by+n)*20,20,20);
                c.strokeRect((bx+m)*20,(by+n)*20,20,20);
            }
        }
    }
}
//--------------------------------------------
//Erase current block before draw new one
//--------------------------------------------
function erase(c,bx,by,dir,kind){
    c.fillStyle="#CC00CC";
    c.strokeStyle="#333333";
    c.lineWidth=3;
    //destination-out: erase mode
    c.globalCompositeOperation="destination-out";
    //actually erase not draw
    draw(c,bx,by,dir,kind);
    //source-over : normal draw mode
    c.globalCompositeOperation="source-over";
}
//--------------------------------------------
//Get the block dropped info 
//--------------------------------------------
function hitConfirm(bx,by,dir,kind){
    p=block[kind][dir];
    for (n=0;n<4;n++){
        for(m=0;m<4;m++){
            if(p[n][m]==1){
                //if over leftside wall or rightsidewall -> false
                if((bx+m<0) || (bx+m >11)){
                    return false;
                };
                //return false if block updown over the top or bottom wall
                if((by+n<0) || (by+n>21)){
                    return false;
                }
                //if the same location of state Array is not vacant (not 100) : false
                if(state[by+n][bx+m] !=100) {
                    return false;
                } 
               
            }
        }
    }
    return true;
}
//--------------------------------------------
//change block's movement  when press arrow keys
//--------------------------------------------
function move(e){
    gamegamen=document.getElementById("game");
    cg=gamegamen.getContext("2d");
    //Save current location
    beforeIx=ix;
    beforeIy=iy;
    beforeDir=idirection;
    //erase current block
    erase(cg,ix,iy,idirection,ikind);
    //letf arrow key <-: move to leftward
    if (e.keyCode ==37) {
        ix--;
    }
    //Up arrow key ^: rotate anticlockwise
    if (e.keyCode ==38) {
        idirection =++idirection % 4 ;
        //The same as code :  if (idirection >3) idirection=0;
    }
    //move to rightward: right arrow key ->
    if (e.keyCode == 39) {
        ix++;
    }
    //Down arrow key v: drop
    if (e.keyCode ==40) {
        dropDown();
    }
    //make sound
    //  document.getElementById("bRotate").play();
    confirm_result=hitConfirm(ix,iy,idirection,ikind)
    if(!confirm_result) // hit , cannot move 
    {
        //recover last position
        ix=beforeIx;
        iy=beforeIy;
        idirection=beforeDir;
    }
     draw(cg,ix,iy,idirection,ikind);
}
//--------------------------------------------
//Drop block control function
//--------------------------------------------
function dropDown(){
    gamegamen=document.getElementById('game');
    cg=gamegamen.getContext('2d');
    //save current position
    ix_before=ix;
    iy_before=iy;
    idir_before=idirection;
    //Clear current shape
    erase(cg,ix,iy,idirection,ikind);
    //move downward
    iy++;
     //make sound
    // document.getElementById("bDrop").play();
    //Check hit below current dropping block
    downward_Hit=hitConfirm(ix,iy,idirection,ikind);
    if (downward_Hit) // can drop 
    {
        draw(cg,ix,iy,idirection,ikind);
    }
    else // hit wall or another block 
    {
        //return last position
        ix=ix_before;
        iy=iy_before;
        idirection=idir_before;
        draw(cg,ix,iy,idirection,ikind);
        //save dropped location to state array by kind value
        p=block[ikind][idirection]
        for (n=0;n<4;n++){
            for (m=0;m<4;m++){
                if(p[n][m] ==1) {
                    state[iy+n][ix+m]=ikind;
                }
            }
        }
         //make sound
        // document.getElementById("bHit").play();
        //Clear filled line and score calculate
        scoreCalc();
        //Show next block
        ix=4;
        iy=0;
        ikind=bnext;
        idirection=0;
        draw(cg,ix,iy,idirection,ikind);
        //Check hit again
        isCanDrop=hitConfirm(ix,iy,idirection,ikind);
        if(!isCanDrop) {
            //As overllaped -> Game Over
            //make sound
            // document.getElementById("bOver").play();
            alert("GAME OVER!");
            isContinue =false;
        }
        //Prepare next block
        nextShape();
        //increase drop speed gradually
        times--;
        if (times <50) {
            //return origin state 1s
            times =1000;
        }
    };   
}
//--------------------------------------------
//Calculate scores
//----------------------------------------
function scoreCalc(){
    filledlineNums=0; // 1 line : 10 point, 2: 20p, 3: 100p, 4:1000p
    //Check all lines
    for (y=0;y<21;y++){
        isNotfullfilled =false;
        for (x=1;x<=10;x++){
            //still not full occupied
            if (state[y][x] == 100 || state[y][x] == 99) {
                isNotfullfilled=true;
            }
        }
        if(!isNotfullfilled) {
            filledlineNums++;
            //make sound
            // document.getElementById("bFilled").play();
            //replace filled line by upper one => check all lines above fullfilled line for state array
            for (k=y;k>0;k--){
                for (x=1;x<=10;x++){
                    state[k][x]=state[k-1][x];
                }
            }
        } 
    }
    //Reset game display
    gamegamen=document.getElementById('game');
    cg=gamegamen.getContext('2d');
    cg.clearRect(0,0,239,439);
    //Reallocate existed blocks
    for (y=0;y<22;y++){
        for (x=0;x<12;x++){
            if (state[y][x] !=100 && state[y][x] != 99) {
                cg.fillStyle=bColor[state[y][x]];
                cg.strokeStyle='#333333';
                cg.lineWidth=3;
                cg.fillRect(x*20,y*20,20,20);
                cg.strokeRect(x*20,y*20,20,20);
            }
        }
    }
    //Score Calculate
    switch(filledlineNums){
        case 1:
            score +=10;
            break;
        case 2:
            score+=20;
            break;
        case 3:
            score +=100;
            break;
        case 4:
            score +=1000;
            //make sound
            // document.getElementById("bAllFilled").play();
    }
    //Show score points
    tgamen=document.getElementById("score");
    tgamen.innerHTML=score;
}