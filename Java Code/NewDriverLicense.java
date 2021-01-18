package Challenge;

import java.util.*;

public class NewDriverLicense {
    
    public static void main(String[] args ){
        final int WATTING_TIME=20;
        List<String>  peoples= new ArrayList<>();
        Scanner sc= new Scanner(System.in);
        String name=sc.nextLine();
        String agents_Str=sc.nextLine();
        String[] others=sc.nextLine().trim().split(" ");
        for (String st : others){
            peoples.add(st);
        }
        peoples.add(name);
        Collections.sort(peoples);
        int my_order=peoples.indexOf(name);
        int agents=Integer.parseInt(agents_Str);
        int my_group= my_order / agents;
        System.out.println((my_group+1)*WATTING_TIME);
        sc.close();
    }
}
