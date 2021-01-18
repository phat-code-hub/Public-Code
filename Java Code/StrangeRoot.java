package Challenge;

import java.util.Scanner;

public class StrangeRoot {
    // Checking Method
    static void isStrange(int number){
        String answer="false";
        long sq=(long) Math.pow(number, 2);
        double sqrt=Math.sqrt(number);
        // Convert numbers to String 
        String sq_str=String.valueOf(sq);
        String sqrt_str=String.format( "%.3f", sqrt);
        String st;
        // iterate square root members , check if square number contains it  or not 
        for(int index=0;index<sqrt_str.length();index++){
            st=String.valueOf(sqrt_str.charAt(index));
            if (sq_str.contains(st)){
                answer="true";
                break;
            }
        }
        System.out.println(answer);
    }
    //Main Code
    public static void main(String[] args) {
        System.out.print("Enter Integer number: ");
        Scanner sc=new Scanner(System.in);
        try {
            int num=sc.nextInt();
            isStrange(num);
        }catch (Exception e) {
            e.printStackTrace();
        }
        finally {
            sc.close();
        }
    }
}
