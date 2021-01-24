package Challenge;

import java.util.Scanner;

public class HoverCraft {
    public static void main (String[] args){
        final int PRICE = 3_000_000;
        final int INSURANCE = 1_000_000;
        final int MONTHLY_CAPACITY = 10;
        final int UNIT_COST = 2_000_000;
        Scanner sc = new Scanner(System.in);
        int customer=sc.nextInt();
        int expence=MONTHLY_CAPACITY*UNIT_COST + INSURANCE;
        int income=customer*PRICE;
        String ans="";
        if (income > expence) ans ="Profit";
        else if (income == expence) ans ="Broken Even";
        else ans = "Loss";
        System.out.println(ans);
        sc.close();
    }
}
