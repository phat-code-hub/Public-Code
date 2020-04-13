import java.util.Scanner;

public class Remove_Space1 {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		System.out.print("String: ");
		String string=sc.nextLine();
		sc.close();
		// can use regex as " " or "\\s"
		String result=string.replaceAll(" ", "");
		System.out.println("After remove spaces :"+ result);
	}

}
