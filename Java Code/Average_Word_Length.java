package Challenge;

import java.util.Scanner;

public class Average_Word_Length {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        try {
            String phrase=sc.nextLine().trim();
            // calculate  number of words seperate by space
            String[] words=phrase.split(" ");
            int str_len=0;
            for (char ch : phrase.toCharArray()){
                // increment len if it is non punctuation
                if (Character.isLetter(ch) && ch!=' ') {
                    str_len++;
                }
            }
            //Convert average to double 
            double res=(double) (str_len)/(double) words.length;
            //Show result by converting ceiling resutlt to int 
            System.out.println((int) Math.ceil(res));
        }
        finally {
            sc.close();
        }
        
    }
}
