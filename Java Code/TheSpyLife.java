package Challenge;

import java.util.Scanner;

public class TheSpyLife {
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);
        String message=sc.nextLine().trim();
        String spyLife=""; 
        for (char c:message.toCharArray()){
            if(Character.isAlphabetic(c)|| c==' '){
                spyLife =c +spyLife;
            }
        }
        System.out.println(spyLife);
        sc.close();
    }
}
