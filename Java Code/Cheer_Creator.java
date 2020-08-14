import java.util.Scanner;

public class Cheer_Creator {
	
	public static void main(String[] args) {
		String sound="";
		Scanner input = new Scanner(System.in);
		int yard=input.nextInt();
		input.close();
		if (yard >10) {
			sound="High Five";
		} else if(yard <1) {
			sound="shh";
		} else {
			for (int i=1; i<=yard;i++) {
				sound += "Ra!";
			}
		};
		System.out.println(sound);

	}

}
