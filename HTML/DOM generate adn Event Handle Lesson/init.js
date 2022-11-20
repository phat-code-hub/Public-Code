
//To see clearly, it should be divide colors array into 2 areas with black divisor : front area is light colors and vice versa 
const colors =["white","red","cyan","yellow","orange","beige","black","gray","purple","brown","green","blue"] // Optional
const ROW =5; //default row number
const COL =5; // default column number
const CELL_SIZE = 50 // default cell size 50px
var COL_LIMIT=5 ;// max display column number
var blackindex=0;// index of black color to see text color clearly
var index =0;// color index
var mode = false; // get next index by choice sequentially , false : by random
var info; // Show result
var rr; //row element
var cc; //column element
var rows,cols;// setting rows , columns
var table; //table variable

//Init function
function init() {
    COL_LIMIT=Math.floor(screen.availWidth/CELL_SIZE); // limit numbers of columns 
    info = document.getElementById("info");
    table= document.getElementById("board");
    blackindex = colors.indexOf("black");
    rr=document.getElementById("rowId");
    cc=document.getElementById("colId");
    //Tool tip for inputting
    rr.title ="number of row (>0)";
    cc.title ="number of column (>0 and <="+COL_LIMIT+")";
}

//Create Table
function initTable() {
    if (table.childNodes.length>0) removeTable();
    rows = rr.value >0?rr.value:ROW;
    cols = cc.value>0?cc.value:COL;
    // if column number larger than Limit set it to COL_LIMIT
    cols =Math.min(cols,COL_LIMIT); 
    createTable(rows,cols);

    // pratice : by your own please create procedure to alert message when input value is 0 or larger than COL_LIMIT
}

//Remove exist table
function removeTable() {
    table.innerHTML ="";
}

//Create new table
function createTable(row,column){ 
    for (let i=0; i<row;i++) {
        // Create line
        var tr = document.createElement("tr");
        for (var j=0;j<column;j++){
            var td = document.createElement("td");
            //record index as cell's id
            td.id = i*row+j;
            //Add column into row
            tr.appendChild(td);
            td.style.width =CELL_SIZE+"px";
            td.style.height=CELL_SIZE+"px";
            td.style.textAlign="center";
            td.title ="cell"+td.id+" :click to get cell color and color text"
            td.onclick =getInfo; // note :function without parentheses ()
            //Same setting as above code
            // td.addEventListener("click",getInfo);
        }
        //Add row into table
        table.appendChild(tr);

    }


//Show cell info (index , color)  
function getInfo(e){
    index = getIndex(mode);
    info.innerText="Cell "+e.target.id +" clicked!";
    info.style.color = colors[index];
    e.target.style.background =colors[index];
    if(index >=blackindex ) e.target.style.color =colors[0]; // White text
    else  e.target.style.color =colors[blackindex]; // default text
    
    if (index==0) e.target.style.color=colors[blackindex]
    else e.target.textContent=colors[index];
}
//Get random index -> sequence =true : get index sequently

function getIndex (sequence=true){
    if (!sequence) {
        return Math.floor(Math.random() * colors.length) ;
    }
    return  index%colors.length;
}
}