import java.util.Scanner;

public class Remove_Space2 {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		System.out.print("String: ");
		String string=sc.nextLine();
		sc.close();
		// replace character in the string
		String result=string.replace(" ", "");
		System.out.println("After remove spaces :"+ result);
	}

}
