// import java.util.*;

import java.util.Scanner;

public class No_Numerals {
    final static String[] digits ={"10","0","1","2","3","4","5","6","7","8","9"};
    final static String[] words ={"ten","zero","one","two","three","four","five","six","seven","eight","nine"};


    static String replaceString(String source ){
        int ind=0;
        StringBuilder sb = new StringBuilder(source);
        for (int i=0; i<digits.length;i++){
            ind = sb.indexOf(digits[i],ind);
            while (ind>=0) {
                sb.replace(ind,ind+digits[i].length(),words[i]);
                ind = sb.indexOf(digits[i],ind);
            }
        }

        return sb.toString();
    }
    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);
        String text = sc.nextLine();
        System.out.println(replaceString(text));
        sc.close();
    }
}
