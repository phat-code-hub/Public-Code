package Challenge;

import java.util.Scanner;

public class PasswordValidation2 {
    static String checkPassword(final String word){
        final String SpecialWords="!@#$%&*";
        final char[] chars= word.toCharArray();
        int sum1=0,sum2=0;
        for (char c: chars){
            if (SpecialWords.contains(Character.toString(c))) sum1++;
            if(Character.isDigit(c)) sum2++;
        }
        return  (word.trim().length()>=7 && sum1 >=2 && sum2 >=2)==true? "Strong":"Weak" ;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String password=sc.nextLine().trim().toLowerCase();
        System.out.println(checkPassword(password));
        sc.close();
    }
}
