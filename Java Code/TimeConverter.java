package Challenge;

import java.util.Scanner;

public class TimeConverter {
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        try {
            int days=sc.nextInt();
            long seconds= days*24*60*60;
            System.out.println(seconds);
        } finally {
            sc.close();
        }
    }
}
