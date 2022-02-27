const CELL=40; //canvas Cell size  default 40
const imgFol="https://raw.githubusercontent.com/phat-code-hub/CodeData/main/SokoBan/";
const imgList= {"Wall": [6,"Wall.png"],
                "Goal": [1,"Goal.png"],
                "Luggage":[2,"Luggage.png"],
                "ManL": [-3,"ManL.png"],
                "ManU":[5,"ManU.png"],
                "ManR":[3,"ManR.png"],
                "ManD":[-5,"ManD.png"]
                }
const direct_arr={ // Moving direction index
    37:-3,
    38:5,
    39:3,
    40:-5
}
var ctx,gc; // Canvas
var rootData; // Data define
var data=[];//dat to Event handle 
var data0=[];//data to draw image on canvas
var px,py; //Worker Starting position
var dx0,dy0;//Worker calculate coordinate argument 
var dx1,dy1; //Luggage in front  Worker  calculate coordinate argument
var images ={};
var curLevel =1; //Current Level EASY
var curStage =1 //Current scence
var curData ="";//Current Scence Data
var direction ; //Direction of worker
var step=0,steps; // count number of walked step
var goalNo=0,filled=0, filled_state; // check filling up all of goal 
var isPushed =false // Luggage was pushed or not
var isUndo = false;// press Undo or not event
//Coordinate of Worker and Luggage  
class Cord {
    constructor(x, y,dir) {
        this.x = x;
        this.y = y;
        this.dir = dir;
    }
}
class History {
    constructor(d,c){
       this.data=d;
       this.Cord= c;
    }
}
var hist0;
var hist=[];
var popHistD=[];
var popHistC;
var histCount=0;
var curCord;//Worker Position
var curLugCord;//Luggage Position