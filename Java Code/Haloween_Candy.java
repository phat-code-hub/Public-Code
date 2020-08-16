import java.util.Scanner;

public class Haloween_Candy {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		double houses=sc.nextDouble();
		sc.close();
		if (houses>=3) {
			System.out.println(Math.round((2/houses)*100));
		}else {
			System.out.println(0);
		}

	}

}
