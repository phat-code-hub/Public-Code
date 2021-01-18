package Challenge;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Prime_String2 {
    static String text;
    static int len;
    static String ans="prime";
    //-----------------------------------------
    static void checkPrime(){
        //First sub_string is a half of text
        int sub_Length=text.length()/2;
        Set<String> set=null;
        do {
            set=new HashSet<>(); // otain sub String created from input text
            if (len % sub_Length ==0) // Check not prime condition
             {
                 for (int i =1;i<=len;i+=sub_Length){
                    set.add(text.substring(i-1,i+sub_Length-1)); // add subtsrings to set
                 }
                 //Check not prime 
                 if (set.size()==1){
                     ans="Not prime"; // if found exit
                     break;
                 }
            }
            sub_Length--;
        } while(sub_Length>0); // loop until substring 's length is 1'

    }
    //----------------------------------------------------------
    //Main code
    public static void main( String[] args) {
        Scanner sc = new Scanner(System.in);
        try{
            System.out.print("Enter text: ");
            text=sc.nextLine().trim();
            len=text.length();
            if (len>0) {
                checkPrime();
            }
            System.out.println(ans);
        }
        finally{
            sc.close();
        }   
    }
    
   
}
