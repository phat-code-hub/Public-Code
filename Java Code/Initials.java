import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class Initials {
    static void  FirstChars(List<String> list) {
    	List<String> temp=new ArrayList<>();
    	list.stream()
    		.forEach(ch-> {
    			String first="";
    			String[] words= ch.split(" ");
    			for (String word:words) if (word!="") first+=word.toUpperCase().charAt(0);
    			temp.add(first);
    		});
    	String InitialsList=String.join(" ", temp);
		System.out.print(InitialsList);
    }
	public static void main(String[] args) {
		List<String >  names=new ArrayList<>();
		try {		
			Scanner sc=new Scanner(System.in);
			String n_=sc.nextLine().trim();
			int n=Integer.parseInt(n_);
			for(int i=0;i<n;i++) {
				names.add(sc.nextLine());
			}
			sc.close();
			FirstChars(names);
		}catch (Exception e ) {
			e.printStackTrace();
		}
	}

}
