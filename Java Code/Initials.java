import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class Initials {
    static List<String>  FirstChars(List<String> list) {
    	List<String> temp=new ArrayList<>();
    	list.stream()
    		.forEach(ch-> {
    			String first="";
    			String[] words= ch.split(" ");
    			for (String word:words) if (word!="") first+=word.toUpperCase().charAt(0);
    			temp.add(first);
    		});
    	return temp;
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
			List<String> Firstname=FirstChars(names);
			String InitialsList=String.join(" ", Firstname);
			System.out.print(InitialsList);
		}catch (Exception e ) {
			e.printStackTrace();
		}
	}

}
