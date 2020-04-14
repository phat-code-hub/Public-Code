import java.util.regex.*;

public class Password_Validation {

	public static void main(String[] args) {
		String word="Nguyen D12uy :Phat :HO56ng Thuy";
		//Pattern pat=Pattern.compile(".{5,100}");
		Pattern pat=Pattern.compile(".*\\d+.*");
		Matcher mat=pat.matcher(word);
//		while(mat.find()) {
//			String st =mat.group();
//			System.out.println(st);
//		}
		boolean res=mat.matches();
		if (res) {
			System.out.println("OK");

		}else {
			System.out.println("NG");
		}

	}

}
