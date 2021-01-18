package Challenge;

import java.util.Scanner;

public class HexColorCodeGenerator {
        public static void main(String[] args){
            Scanner sc= new Scanner(System.in);
            int[] colors=new int[3];
            String[] hex_colors= new String[3];
            for (int i=0;i<3;i++){
                colors[i] =sc.nextInt();
            }
           sc.close();
           for (int i=0;i<colors.length;i++){
               hex_colors[i]=Integer.toHexString(colors[i]);
           }
           System.out.println("#"+String.join("",hex_colors));
        }
}
