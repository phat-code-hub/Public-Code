import java.util.*;
import java.util.regex.*;

public class Password_Validator {
	static final String SpecialChars = "<([{#%_~@&\\^$!|]})?*+.>";
	public static void main(String[] args) {
		System.out.print("Password:");
		Scanner sc=new Scanner(System.in);
		String word=sc.nextLine();
		sc.close();
		String[] pat= {"^.{5,10}$", // 5 to 10 letters
				"(.)*\\d+(.)*", // at least 1 number
				"(.)*["+SpecialChars+"]+(.)*$", // at least 1 special letter
				"\\S+"}; // not blank
		Pattern p = null;
	    Matcher m=null;
		List<Boolean> isMatch=new ArrayList<>();
		for (String st: pat) {
			p=Pattern.compile(st);
			m=p.matcher(word);
			isMatch.add(m.matches());
			m.reset(word);
		}
		System.out.println(isMatch.stream().allMatch(x ->x ==true));
	}

}