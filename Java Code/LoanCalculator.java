package Challenge;

import java.util.Scanner;

public class LoanCalculator {
    static double RATE=0.1;// 10%
    static int MONTHS=6;
    public static void main (String[] args) {
        System.out.print("Enter borrow amount: ");
        Scanner scanner= new Scanner(System.in);
        int amount=scanner.nextInt();
        System.out.print("How many months to pay back (6)? ");
        int limit =scanner.nextInt() ;
        MONTHS=limit>0 ?limit:6;
        System.out.print("Interest rate:(10%)? ");
        double rate=scanner.nextDouble();
        RATE = (rate >1) ? rate/100:rate;
        int payment;
        int remain=amount;
        int month=1;
        System.out.println("---------------------------------");
        System.out.printf("Within %s months and %.2f  rate :\n",MONTHS,RATE);
        do {
            payment=(int) Math.ceil(remain*RATE);
            remain =(int) (remain-payment);
            if (remain != 0) 
                System.out.printf("Month %d => Paid: %d ,Remain: %d\n",month,payment,remain);
        } while ((++month<=MONTHS) && (remain >0) );
        System.out.println("Unpaid remaining: "+remain);
        scanner.close();
    }
}
