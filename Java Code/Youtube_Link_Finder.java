import java.util.Scanner;
public class Youtube_Link_Finder {
	
	public static void main(String[] args) {
		String link_str;
		Scanner sc =new Scanner(System.in);
		try {
			link_str=sc.nextLine().trim();
			String find_pattern="watch?v=";
			int i=link_str.lastIndexOf(find_pattern);
			if (i>-1) {
				System.out.println(link_str.substring(i+find_pattern.length()));
			} else {
				String[] groups=link_str.split("/");
				System.out.println(groups[groups.length-1]);	
			}	
		}
		finally {
			sc.close();
		}
		}
	}
