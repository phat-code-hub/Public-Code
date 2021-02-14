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
var curMenu=1;
var curName;
const MIN=0;
const MAX=255;

//Original (primary)  Color
var names=["Black","Silver","Gray","White","Maroon","Red","Purple","Fuchsia",
           "Green","Lime","Olive","Yellow","Navy","Blue","Teal","Aqua","Orange"];
var hex=["000000","C0C0C0","808080","FFFFFF","800000","FF0000","800080","FF00FF",
         "008000","00FF00","808000","FFFF00","000080","0000FF","008080","00FFFF","FFA500"];
var note=names;
//CSS3 Colors
var cnames=["Black","Silver","Gray","White","Maroon","Red","Purple","Fuchsia",
           "Green","Lime","Olive","Yellow","Navy","Blue","Teal","Aqua",
           "Orange","BlanchedAlmond","LightYellow","CornSilk","AntiqueWhite","PapayaWhip","LemonChiffon","Beige",
           "Linen","OldLace","LightCyan","AliceBlue","WhiteSmoke","LavenderBlush","FloralWhite","MintCream",
           "GhostWhite","HoneyDew","SeaShell","Ivory","Azure","Snow","Gainsboro","LightGrey",
           "DarkGrey","LightSlateGrey","SlateGrey","DimGrey","DarkSlateGrey","LawnGreen","GreenYellow","ChartReuse",
           "LimeGreen","YellowGreen","OliveDrab","DarkOliveGreen","ForestGreen","DarkGreen","SeaGreen","MediumSeaGreen",
           "DarkSeaGreen","LightGreen","PaleGreen","SpringGreen","MediumSpringGreen","DarkCyan","LightSeaGreen","MediumAquamarine",
           "CadetBlue","SteelBlue","Aquamarine","PowderBlue","PaleTurquoise","LightBlue","LightSteelBlue","SkyBlue",
           "LightSkyBlue","MediumTurquoise","Turquoise","DarkTurquoise","Crimson","DarkRed","Brown","Sienna",
           "SaddleBrown","IndianRed","RosyBrown","LightCoral","Salmon","DarkSalmon","Coral","Tomato",
           "SandyBrown","LightSalmon","Peru","Chocolate","OrangeRed","DarkOrange","Tan","PeachPuff",
           "Bisque","Moccasin","NavajoWhite","Wheat","BurlyWood","DarkGoldenRod","GoldenRod","Gold",
           "LightGoldenRodYellow","PaleGoldenRod","Khaki","DarkKhaki","Cyan","DeepSkyBlue","DodgerBlue","CornFlowerBlue",
           "RoyalBlue","MediumBlue","DarkBlue","MidnightBlue","DarkSlateBlue","SlateBlue","MediumStateBlue","MediumPurple",
           "DarkOrchid","DarkViolet","BlueViolet","MediumOrchid","Plum","Lavender","Thistle","Orchid",
           "Violet","Indigo","DarkMagenta","MediumVioletRed","DeepPink","Magenta","HotPink","PaleVioletRed",
           "LightPink","Pink","MistyRose"
            ];
var chex=["000000","C0C0C0","808080","FFFFFF","800000","FF0000","800080","FF00FF",
         "008000","00FF00","808000","FFFF00","000080","0000FF","008080","00FFFF",
         "FFA500","FFEBDC","FFFFE0","FFF8DC","FAEBD7","FFEFD5","FFFACD","F5F5DC",
         "FAF0E6","FDF5E6","E0FFFF","F0F8FF","F5F5F5","FFF0F5","FFFAF0","F5FFFA",
         "F8F8FF","F0FFF0","FFF5EE","FFFFF0","F0FFFF","FFFAFA","DCDCDC","D3D3D3",
         "A9A9A9","778899","708090","696969","2F4F4F","7CFC00","ADFF2F","7FFF00",
         "32CD32","9ACD32","6B8E23","556B2F","228B22","006400","2E8B57","3CB371",
         "8FBC8B","90EE90","98FB98","00FF7F","00FA9A","008B8B","20B2AA","66CDAA",
         "5F9EA0","4682B4","7FFFD4","B0E0E6","AFEEEE","ADD8E6","B0C4DE","87CEEB",
         "87CEFA","48D1CC","40E0D0","00CED1","DC143C","8B0000","A52A2A","A0522D",
         "8B4513","CD5C5C","BC8F8F","F08080","FA8072","E9967A","FF7F50","FF6347",
         "F4A460","FFA07A","CD853F","D2691E","FF4500","FF8C00","D2B48C","FFDAB9",
         "FFE4C4","FFE4B5","FFDEAD","F5DEB3","DEB887","B8860B","DAA520","FFD700",
         "FAFAD2","EEE8AA","F0E68C","BDB76B","00FFFF","00BFFF","1E90FF","6090EF",
         "4169E1","0000CD","00008B","191970","483D8B","6A5ACD","0E00B0","9370DB",
         "9932CC","9400D3","8A2BE2","BA55D3","DDA0DD","E6E6FA","D8BFD8","DA70D6",
         "EE82EE","4B0082","8B008B","C71585","FF1493","FF00FF","FF69B4","DB7093",
         "FFB6C1","FFC0CB","FFE4E1"
            ];
var cnote=cnames;
//Japanese style Color       
var jnames=["UsuiGaki","Arazome","BeniEbiCha","Suou","AsaSuou","Shinku","EbiIro","GinShu",
            "Enji","AkaneIro","Kokihi","ShoujouHi","Aka","BeniAka","Kurenai","KaraKurenai"
     ];
var jhex=["D4ACAD","D69090","A73836","9E3D3F","A25768","A22041","640125","C85554",
            "B94047","B7282E","C9171E","E2041B","E60033","D9333F","D7003A","E95464"
     ]
var jnote=["薄柿","退紅","紅海老茶","蘇芳","浅蘇芳","真紅","葡萄色","銀朱",
            "臙脂","茜色","深緋","猩々緋","赤","紅赤","紅","韓紅"
  ];
//Foreign style Color use in Japan       
var fnames=["Coral_F","Poopy","Red_F","Tomato_F","Vermilion","Scarlet","Carrot","Chinese",
            "Terracotta","Cocoa","Mahogany","Chocolate_F","Marron","Sepia","Coffee","Brown_F",
     ];
var fhex=["EF857D","EA5550","EA5550","EA5549","EA553A","EA5532","ED6D35","ED6D46",
            "BD6856","98605E","6B3F31","6C3524","6A1917","622D18","7B5544","8F6552"
     ]
var fnote=["コーラレレッド","ポピーレッド","レッド","トマトレッド","バーミリオン","スカーレッド","キャロットオレンジ","チャイニーズレッド",
            "テラコッタ","ココアブラウン","マホガニー","チョコレート","マルーン","セピア","コーヒー色","ブラウン"
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
            curMenu=i;
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
        case 2: // CSS
        {
            lstName=cnames;
            lstValue=chex;
            lstNote=cnote;
            break;
        }
        case 3: // Japan
        {
            lstName=jnames;
            lstValue=jhex;
            lstNote=jnote;
            break;
        }
        case 4: // foreign
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
        name:cnames.concat(jnames,fnames),
        hexValue:chex.concat(jhex,fhex),
        note:cnote.concat(jnote,fnote),
        kind:[]
    }
    let kind_Len=[];
    kind_Len[0]=cnames.length;
    kind_Len[1]=jnames.length;
    kind_Len[2]=fnames.length;
    for (var i=0;i<kind_Len.length;i++){
        for (var j=0;j<kind_Len[i];j++){
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
    explain[1]="17 Basic (primary) colors\n"+
            "'Orange' was added  from CSS2.1";
    explain[2]="Colors defined from CSS3\n(include basic colors)";
    explain[3]="Japanese style named color<br>" +
                "They follow JIS standard and named by 'Kanji' words";
    explain[4]="Common abroad_based named colors used in japan<br>" +
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
        if (allList.name[index] !== curName ){
            let index2 = allList.hexValue.lastIndexOf(value.toUpperCase());
            str= allList.name[index2];
        } else  {
             str= allList.name[index];
        }
        switch (allList.kind[index]){
            case 0: {
                let ind=hex.indexOf(value.toUpperCase())
                let bname=names[ind];
                if (ind >=0 && bname === curName){
                    str += "(Basic)";
                }
                break;
            }
            case 1: {
                str += "(Japan)";
                break;
            }
            case 2: {
                str += "(foreign)";
                break;
            }
        };
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
    curName= selectItem[selectItem.selectedIndex].text;
    let curValue=document.getElementById("choice").value;
    document.getElementById("tred").value=curValue.substring(0,2);
    update(0,2);
    document.getElementById("tgreen").value=curValue.substring(2,4);
    update(1,2);
    document.getElementById("tblue").value=curValue.substring(4);
    update(2,2);
}
//------------------------------------------------------
//Show added color numbers
//------------------------------------------------------
function showCount(){
    this.event.target.title=selectItem.options.length+" colors";
}
//------------------------------------------------------
//Show selected color's info
//------------------------------------------------------
function info(num=3) {
    let msg,rgb,note,name; 
    switch (num) {
        case 0: //mouse on range
        {
            this.event.target.title=this.event.target.length;
            break;
        }
        case 1: // mouse on number
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
                let jp_name="";
                if ((curMenu>2) || ((curMenu == 0) && (allList.kind[index]>=1))) {
                    jp_name="\nJapanese Name: "+ note;
                } 
                msg=name+"\n"+rgb+"\nHex Value: #"+hex_Str+jp_name;
            } 
            else {
                name=hex_result.innerHTML;
                msg=name+"\n"+rgb;
            } 
            this.event.target.title=msg
        }
       
    }
}


