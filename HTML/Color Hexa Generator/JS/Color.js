var red,green,blue;
var color_Element;
var text_Element;
var tip;
var hexval;
//------------------------------------------------------
//Initialize color
//------------------------------------------------------
window.onload =function() {
    color_Element=document.getElementById("color");
    text_Element=document.getElementById("hex");
    changeColor();
}
//------------------------------------------------------
//Change the color by changing values
//------------------------------------------------------
function change( n){
    var source;
    var desc;
    switch(n){
        case 1:{
            source=document.getElementById("rred");
            desc=document.getElementById("nred");
            break;
        }
        case 2:{
            source=document.getElementById("nred");
            desc=document.getElementById("rred");
            break;
        }
        case 3:{
            source=document.getElementById("rgreen");
            desc=document.getElementById("ngreen");
            break;
        }
        case 4:{
            source=document.getElementById("ngreen");
            desc=document.getElementById("rgreen");
            break;
        }
        case 5:{
            source=document.getElementById("rblue");
            desc=document.getElementById("nblue");
            break;
        }
        case 6:{
            source=document.getElementById("nblue");
            desc=document.getElementById("rblue");
        }
    }
    desc.value=source.value;
    changeColor();
} 
//------------------------------------------------------
//Show seleted decimal value of range input 
//------------------------------------------------------
function show(value){
    switch (value){
        case 1:{
            tip=document.getElementById("rred");
            break;
        }
        case 2:{
            tip=document.getElementById("rgreen");
            break;
        }
        default:{
            tip=document.getElementById("rblue");
        }
    }
    tip.title=tip.value;
}
//------------------------------------------------------
//Show seleted hex value of number input 
//------------------------------------------------------
function showHex(value) {
    let el;
    switch (value){
        case 1:{
            el=document.getElementById("nred");
            break;
        }
        case 2:{
            el=document.getElementById("ngreen");
            break;
        }
        default:{
            el=document.getElementById("nblue");
        }
    }
    let dec_val=el.value;
    tip="hex value= "+Number(dec_val).toString(16);
    el.title=tip;
}
//------------------------------------------------------
//Display color by changes values of range or number 
//------------------------------------------------------
function changeColor(){
    red=document.getElementById("rred").value;
    green=document.getElementById("rgreen").value;
    blue=document.getElementById("rblue").value;
    hexValue(red,green,blue);
    var colours="rgb("+red+","+green+","+blue+")";
    color_Element.style.backgroundColor=colours;
    tip=colours+"\nHex name : "+hexval;
    color_Element.title=tip;
    text_Element.style.color=colours;
}
//------------------------------------------------------
//Show Hex value of selected color
//------------------------------------------------------
function hexValue(r,g,b){
    var r_hex=Number(r).toString(16);
    var g_hex=Number(g).toString(16);
    var b_hex=Number(b).toString(16);
    hexval="#"+r_hex+g_hex+b_hex;
    text_Element.innerHTML=hexval;
}