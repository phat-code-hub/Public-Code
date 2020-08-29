import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Youtube_Link_Finder {
	
	public static void main(String[] args) {
		String link_str;
		Scanner sc =new Scanner(System.in);
		try {
			link_str=sc.nextLine().trim();
			String reg=".+[/|?v=]";
			Pattern pat=Pattern.compile(reg);
			Matcher mat=pat.matcher(link_str);
			if (mat.find()) {
				System.out.println(link_str.substring(mat.end()));
			}
		}
		finally {
			sc.close();
		}
		}
	}
