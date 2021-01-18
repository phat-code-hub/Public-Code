package Challenge;

import java.util.Scanner;

public class Kaleidoscope {
    public static void main(String[] args){
        final double TAX=1.07;
        final double DISCOUNT=0.1;
        final double PRICE=5.0;
        Scanner sc = new Scanner(System.in);
        int num=sc.nextInt();
        double sum =num *PRICE;
        if (num>1) sum*= (1-DISCOUNT);
        sum *= TAX;
        // System.out.println(sum);
        System.out.format("%.2f",sum);
        sc.close();
    }
}
