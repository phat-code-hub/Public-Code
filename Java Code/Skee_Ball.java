import java.util.Scanner;

public class Skee_Ball {

	public static void main(String[] args) {
		final int SCALE=12;
		String result="";
		Scanner input= new Scanner(System.in);
		int points=input.nextInt();
		int cost=input.nextInt();
		input.close();
		int received_tickets=points/SCALE;
		if (received_tickets >= cost) result = "Buy it!";
		else result ="Try again";
		System.out.println(result);
	}

}
