package Challenge;

import java.util.Scanner;

public class PigLatin {
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);
        try {
            String[] words= sc.nextLine().split(" ");
            //Check whether Array null or not
            if (words[0].trim().length()>0){
                final String SUBFIX = "ay "; 
                StringBuffer pigLatin = new StringBuffer();
                for (String st:words) {
                    pigLatin.append(st.substring(1)+st.substring(0,1)+SUBFIX);
                }
                //Delete last space and output
                pigLatin=pigLatin.deleteCharAt(pigLatin.length()-1);
                System.out.println(pigLatin);
            }
            
        } catch (Exception e){
            e.printStackTrace();
        }
        finally {
            sc.close();
        }
    }
}
