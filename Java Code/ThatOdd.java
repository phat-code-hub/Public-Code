package Challenge;

import java.util.*;

public class ThatOdd {
    public static void main(String[] args){
        List<Integer> lst=new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int n= Integer.parseInt(sc.nextLine());
        for (int i=0;i<n;i++){
            lst.add(Integer.parseInt(sc.nextLine()));
        }
        int even_sum=lst.stream()
            .filter(x->x%2==0)
            .mapToInt(Integer::intValue)
            .sum();
        System.out.println(even_sum);
        sc.close();
    }
}
