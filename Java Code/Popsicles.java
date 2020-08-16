import java.util.Scanner;

public class Popsicles {

	public static void main(String[] args) {
		String ans="";
		Scanner sc = new Scanner(System.in);
		System.out.print("Siblings Numbers: ");
		int siblings =sc.nextInt();
		System.out.print("Popsicles Numbers: ");
		int popsicles=sc.nextInt();
		sc.close();
		int left = popsicles % siblings;
		int groups=popsicles /siblings;
		if (left >=0 && groups>=2) {
			ans="give away";
		} else {
			ans="eat them yourself";
		}
		System.out.println(ans);
	}

}
