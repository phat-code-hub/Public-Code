import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class It_a_Sign {
	static List<String> names=new ArrayList<>();
	static List<Boolean> result=new ArrayList<>();
    static void isPanlindrome(String st) {
    	StringBuilder chk1=new StringBuilder(st);
    	StringBuilder chk2=new StringBuilder(st);
    	chk2=chk2.reverse();
    	System.out.println(chk1+","+chk2);
    	result.add(chk1.equals(chk2));
    }
	public static void main(String[] args) {
		System.out.println("4 Words Please.");
		Scanner sc=new Scanner(System.in);
		try {
			for (int i=0; i<4;i++) {
				names.add(sc.nextLine());
			}
			names.stream().forEach(s-> isPanlindrome(s.toUpperCase()));
			result.stream().forEach(s-> System.out.println(s));
		}catch (Exception e) {
			
		}finally {
			sc.close();
		}

	}

}
