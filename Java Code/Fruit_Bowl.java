import java.util.Scanner;

public class Fruit_Bowl {

	public static void main(String[] args) {
		Scanner sc= new Scanner (System.in);
		int fruits= sc.nextInt();
		sc.close();
		int apples=(fruits /2) /3;
		System.out.println(apples);
	}

}
