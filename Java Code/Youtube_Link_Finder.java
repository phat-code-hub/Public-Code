import java.util.Scanner;
//import java.util.regex.Matcher;
//import java.util.regex.Pattern;

public class Youtube_Link_Finder {
	
	public static void main(String[] args) {
		String link_str;
		Scanner sc =new Scanner(System.in);
		try {
//			link_str=sc.nextLine().trim();
			link_str="https://www.youtube.com/watch?v=kbx365";
			link_str="https://youtu.be/kbx365";
//			String reg=".+[/|?v=]";
//			Pattern pat=Pattern.compile(reg);
//			Matcher mat=pat.matcher(link_str);
//			if (mat.find()) {
//				System.out.println(link_str.substring(mat.end()));
//			}
			//link_str="abcwatch?v=KBC";
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
