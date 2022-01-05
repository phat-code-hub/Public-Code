<!-- This app is a simple program for analyse
    and return calculated result of Reverse Polish Notation (RPN) format 
    using stack method
    For example : from Normal format  (1+2) * (3+4) = 21 ,if using RPN format  : 12+34+* 
    Created by Ueda
------------------------------- -->
<?php
    // Check Input Data
    $rpn = isset($_GET['rpn'])? $_GET["rpn"]:"1 2 3 * +";
    // RPN Calculate
    $history="";
    $answer = calcRPN($rpn);

    # RPN calculate 
    function calcRPN($str) {
        global $history;
        //  Divide data into small token unit 
        $tokens = preg_split("#\s+#", trim($str)); // Split by space, blank character
        $stack = [];
        foreach ($tokens as $t) {
            //Case of numerical value
            if(preg_match("#^[0-9]+#",$t)) {
                $stack[] = floatval($t);
                addHistory($stack,"$t: push");
                continue;
            }
            //Normal operator
            $b = array_pop($stack);
            $a = array_pop($stack);
            switch($t) {
                case '+': $c = ($a +$b); break; 
                case '-': $c = ($a -$b); break;
                case '*': $c = ($a *$b); break;
                case '/': $c = ($a /$b); break;
                case '%': $c = ($a +$b); break;
                default: return "Error";
            }
            $stack[] = $c;
            addHistory($stack,"$t : pop $a $b , push $c");
        }
        return array_pop($stack);
    }
    #----------------------------
    #Display on Table of page
    function addHistory($stack,$desc) {
        global $history;
        $line = "<td> $desc</td>".
                    "<td>[".implode(", ",$stack)."]</td>";
        $history .= "<tr>".$line."</tr>";
    };
    #----------------------------
    #HTMLPage output
    $rpn = htmlentities($rpn,ENT_QUOTES);
    echo <<< EOS
    <!DOCTYPE html> 
    <meta charset= 'utf-8'>
    <title>Reverse Polish Notation Calculate</title>
    <form>
        RPN : <input name= "rpn" value ="$rpn" size="30"><br>
        <input type = "submit" value = "Calculate">
    </form><hr>
    <div>Answer:<strong><italic> $answer</italic></strong></div><hr>
    <table>
    <tr>
    <td>OPERATE</td>
    <td>STACK</td>
    </tr>
    $history</table>
    EOS
?>