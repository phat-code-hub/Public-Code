var colors=[0,0,0];
var numValue;
var rangeValue;
var hexValue;
var before;
var selectItem;
var selectType;
var allList,list;
var lstName,lstValue,lstNote;
var explain =[];
var comment;
var index;
var hex_Str;
var hex_result;
var systemColors;
const MIN=0;
const MAX=255;

//Original (primary)  Color
var names=["Black","Silver","Gray","White","Maroon","Red","Purple","Fuchsia",
           "Green","Lime","Olive","Yellow","Navy","Blue","Teal","Aqua",
           "Snow","GhostWhite","WhiteSmoke","FloralWhite","Linen","AntiqueWhite","PapayaWhip","BlanchedAlmond",
           "Bisque","Moccasin","NavajoWhite","PeachPuff","MistyRose","LevenderBlush","Seashell","OldLace",
           "Ivory","Honeydew","MintCream","Azure","AliceBlue","Lavender","DarkSlateGray","DimGray",
        ];
var hex=["000000","C0C0C0","808080","FFFFFF","800000","FF0000","800080","FF00FF",
         "008000","00FF00","808000","FFFF00","000080","0000FF","008080","00FFFF",
         "FFFAFA","F8F8FF","F5F5F5","FFFAF0","FAF0F6","FAEBD7","FFEFD5","FFEBCD",
         "FFE4C4","FFE4B5","FFDEAD","FFDAB9","FFE4E1","FFF0F5","FFF5EE","FDF5E6",
         "FFFFF0","F0FFF0","F5FFFA","F0FFFF","F0F8FF","E6E6FA","2F4F4F","696969",
        ]
var note=["Black","Silver","Gray","White","Maroon","Red","Purple","Fuchsia",
        "Green","Lime","Olive","Yellow","Navy","Blue","Teal","Aqua",
        "Snow","GhostWhite","WhiteSmoke","FloralWhite","Linen","AntiqueWhite","PapayaWhip","BlanchedAlmond",
        "Bisque","Moccasin","NavajoWhite","PeachPuff","MistyRose","LevenderBlush","Seashell","OldLace",
        "Ivory","Honeydew","MintCream","Azure","AliceBlue","Lavender","DarkSlateGray","DimGray",
        ];
//Japanese style Color       
var jnames=["UsuiGaki","Arazome","BeniEbiCha","Suou","AsaSuou","Shinku","EbiIro","GinShu"
     ];
var jhex=["D4ACAD","D69090","A73836","9E3D3F","A25768","A22041","640125","C85554"
     ]
var jnote=["薄柿","退紅","紅海老茶","蘇芳","浅蘇芳","真紅","葡萄色","銀朱"
  ];
//Foreign style Color use in Japan       
var fnames=["Coral","Poopy","Tomato","Vermilion","Scarlet","Carrot","Chinese","Terracotta"
     ];
var fhex=["EF857D","EA5550","EA5549","EA553A","EA5532","ED6D35","ED6D46","DB6856"
     ]
var fnote=["Coral","Poopy","Tomato","Vermilion","Scarlet","Carrot","Chinese","Terracotta"
  ];
//------------------------------------------------------
//Show Menu
//------------------------------------------------------
function showMenu(menu=1){
    createOption(menu);
    comment.innerHTML=explain[menu];
}
//------------------------------------------------------
//Clear Menu
//------------------------------------------------------
function clearOptions(){
   if (selectItem.hasChildNodes()){
       while (selectItem.firstChild) {
           selectItem.removeChild(selectItem.firstChild);
       }
   } 
}
//------------------------------------------------------
//Prepare Menu
//------------------------------------------------------
function menu(option = 1){
    for (let i=0;i<systemColors.length;i++){
        if (systemColors[i].checked) {
            clearOptions();
            showMenu(i);
            break;
        }
    }
}
//------------------------------------------------------
//Collect infos 
//------------------------------------------------------
function createOption(type =1){
    switch (type){
        case 0 ://All
        {
            lstName=allList.name;
            lstValue=allList.hexValue;
            lstNote=allList.note;
            break;
        }
        case 2: // Japan
        {
            lstName=jnames;
            lstValue=jhex;
            lstNote=jnote;
            break;
        }
        case 3: // foreign
        {
            lstName=fnames;
            lstValue=fhex;
            lstNote=fnote;
            break;
        }
        default:  //primary
        {
            lstName=names;
            lstValue=hex;
            lstNote=note;
        }
    }
    list.name=[].concat(lstName);
    list.name.sort();
    updateSelectMenu();
    
}
//------------------------------------------------------
//Construct and Update select infos
//------------------------------------------------------
function updateSelectMenu() {
    for (i=0;i<list.name.length;i++){
        var elem=document.createElement("option");
        var str=document.createTextNode(list.name[i]);
        index=lstName.indexOf(list.name[i]);
        list.note.push(lstNote[index]);
        list.hexValue.push(lstValue[index]);
        elem.value=lstValue[index];
        elem.appendChild(str);
        selectItem.appendChild(elem);
    }
    selectItem.value=-1
}
//------------------------------------------------------
//Create info for seraching array allList
//------------------------------------------------------
function searchArray(){
    allList= {
        name:names.concat(jnames,fnames),
        hexValue:hex.concat(jhex,fhex),
        note:note.concat(jnote,fnote),
        kind:[]
    }
    let arr=[];
    arr[0]=names.length;
    arr[1]=jnames.length;
    arr[2]=fnames.length;
    for (var i=0;i<arr.length;i++){
        for (var j=0;j<arr[i];j++){
            allList.kind.push(i);
        }
    }
}
//------------------------------------------------------
//Init
//------------------------------------------------------
window.onload =function(){
    numValue=document.getElementsByClassName("number");
    rangeValue=document.getElementsByClassName("range");
    hexValue=document.getElementsByClassName("hex");
    comment=document.getElementById("explain");
    systemColors=document.getElementsByName("kind");
    selectItem=document.getElementById("choice");
    hex_result=document.getElementById("hexText");
    explain[0]="All available listed named colors"
    explain[1]="Common named color names (primary colors)"
    explain[2]="Japanese style named color<br>" +
                "They follow JIS standard and named by 'Kanji' words";
    explain[3]="Common abroad_based named colors used in japan<br>" +
            "They follow JIS standard and named by 'Katakana' words"
    numValue[0].value=Math.floor(Math.random()*256);
    numValue[1].value=Math.floor(Math.random()*256);
    numValue[2].value=Math.floor(Math.random()*256);
    for (i=0;i<numValue.length;i++){
        colors[i]=numValue[i].value;
    }
    for (j=0;j<numValue.length;j++){
        rangeValue[j].value=colors[j];
        hexValue[j].value=pad(Number(colors[j]).toString(16));
    }
    //All info obtain object
    searchArray()
    //List Normal named colors
    list ={
        name :[],
        hexValue:[],
        note:[]
    }
    // createOption();
    showMenu();
    show()
}
//------------------------------------------------------
//Fill 0 left of 1 letter string
//------------------------------------------------------
function pad(num){
    return num.length<2?"0"+num:num; 
}
//------------------------------------------------------
//Check input error  
//------------------------------------------------------
function isValid(value,type=1){
    if (type <2) // int value
        { 
            return (MIN<=value && value<=MAX);
        } 
    else  // hex Value 
        {
            return !isNaN("0x"+value);
        }
}

//------------------------------------------------------
//Update color values to array colors  
//------------------------------------------------------
function update(basic,inputType=1){
    switch(inputType){
        case 0: //Range 
            {
                colors[basic]=rangeValue[basic].value;
                numValue[basic].value=colors[basic];
                hexValue[basic].value=pad(Number(colors[basic]).toString(16));
                break;
            }
        case 1:  // change Number input 
            {
                if (isValid(numValue[basic].value)){
                    colors[basic]=numValue[basic].value;              
                }
                else {
                    alert("InValid!\nValue must be between "+MIN +" and "+MAX);
                    colors[basic]=MIN;
                    numValue[basic].value=MIN;         
                }
                rangeValue[basic].value=colors[basic];
                hexValue[basic].value=pad(Number(colors[basic]).toString(16));
                break;
            }
        case 2: // Change hex Input
         {
            if (isValid(hexValue[basic].value,2)) {
                colors[basic]=parseInt(hexValue[basic].value,16);
                numValue[basic].value=colors[basic];
                rangeValue[basic].value=colors[basic];
                hexValue[basic].value=pad(colors[basic].toString(16));
            } else {
                alert("InValid!\nHex value must be between '00' and'ff'");
                color[basic]=MIN;
                numValue[basic].value=MIN;
                rangeValue[basic].value=MIN;
                hexValue[basic].value=pad(Number(0).toString(16));
            }
            
             break;
         }

    }
    show();
}

//------------------------------------------------------
//Show color from number input value  
//------------------------------------------------------
function show(){
    var colours="rgb("+colors[0]+","+colors[1]+","+colors[2]+")";
    document.getElementById("color").style.backgroundColor=colours;
    let hex_value=hexValueConvert();
    hex_result.innerHTML=updateValue(hex_value);
}
//------------------------------------------------------
//Search color name after changing values
//------------------------------------------------------
function updateValue(value){
    index = allList.hexValue.indexOf(value.toUpperCase());
    let str="#"+value;
    if (index >=0) {
        str= allList.name[index];
        if (allList.kind[index] == 1){
            str += "(Japan)";
        } else if (allList.kind[index] == 2){
            str += "(foreign)";
        }
    }
    return str;
}
//------------------------------------------------------
//Convert color values from integer to Hex String
//------------------------------------------------------
function hexValueConvert(){
    hex_Str="";
    for (i=0;i<3;i++){
        hex_Str+=hexValue[i].value;
    }
    return hex_Str;
}
//------------------------------------------------------
//Change color by choose from option list
//------------------------------------------------------
function showName(){
    let mau=document.getElementById("choice").value;
    document.getElementById("tred").value=mau.substring(0,2);
    update(0,2);
    document.getElementById("tgreen").value=mau.substring(2,4);
    update(1,2);
    document.getElementById("tblue").value=mau.substring(4);
    update(2,2);
}
////------------------------------------------------------
//Show selected color's info
//------------------------------------------------------
function info(num=3) {
    let msg,rgb,note,name; 
    // hex_result=document.getElementById("hexText");
    switch (num) {
        case 1: // mouse on number or range
        {   
            this.event.target.title="Value is from 0 to 255";
            break;
        }
        case 2: // mouse on hex input text
        {
            this.event.target.title="Hex value is from '00' to 'ff'";
            break;
        }
        default: // mouse on name label
        {
            rgb="rgb("+colors[0]+","+colors[1]+","+colors[2]+")";
            if (index > -1) {
                name=allList.name[index];
                note=allList.note[index];
                msg=name+"\n"+rgb+"\nHex Value: #"+hex_Str+"\nJapanese Name: "+ note;
            } 
            else {
                name=hex_result.innerHTML;
                msg=name+"\n"+rgb;//+"\nHex Value: "+hex_Str+"\nJapanese Name: "+ note;
            } 
           
            hex_result.title=msg;
        }
       
    }
}


