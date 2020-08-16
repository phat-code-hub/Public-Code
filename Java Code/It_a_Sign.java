import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class It_a_Sign {
	static List<String> names=new ArrayList<>();
	static List<Integer> result=new ArrayList<>();
    static void isPanlindrome(String st) {
    	StringBuilder chk1=new StringBuilder(st);
    	StringBuilder chk2=new StringBuilder(st);
    	chk2=chk2.reverse();
    	result.add(chk1.compareTo(chk2));
    }
	public static void main(String[] args) {
		boolean answer;
		Scanner sc=new Scanner(System.in);
		try {
			for (int i=0; i<4;i++) {
				names.add(sc.nextLine());
			}
			names.stream().forEach(s-> isPanlindrome(s.toUpperCase()));
			answer= result.stream().anyMatch(n -> n==0);
			System.out.println(answer?"Open":"Trash");	
		}catch (Exception e) {
			e.printStackTrace();
		}finally {
			sc.close();
		}

	}

}
