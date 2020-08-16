import java.util.Scanner;

public class Collatz_Conjenture {
	static void showResult(int num) {
		int step=0;
		int before=num;
		int after=num;
		String op="";
		while(before >1) {
			if (before % 2 == 0) {
				op=" / 2 + = ";
				after=before /2;
			}else {
				op=" * 3 + 1 = ";
				after=before *3 +1;
			}
			step++;
			System.out.println("Step "+ step+": " +before+op+after);
			before=after;
		}
		System.out.println();
		System.out.printf("After %d steps , %d reached to 1",step,num);
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		try {
			System.out.print("Enter natural number: ");
			int num=sc.nextInt();
			if (num ==1) {
				System.out.println("1 is final goal!");
			}else if (num >1) {
				System.out.println();
				showResult(num);
			}else {
				System.out.println(num +" is not a natural number!");
			}
		}catch (Exception e) {
			System.out.println("Invalid natural number format!");
		} finally {
			sc.close();
		}
	}
}
