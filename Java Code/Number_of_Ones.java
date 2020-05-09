import java.util.Scanner;

public class Number_of_Ones {
	static String bin(int n) {
		String bin="";
		int temp=n;
		while (true ) {
			int b= temp % 2;
			bin=Integer.toString(b)+bin;
			temp=temp /2;
			if (temp ==0) break;
		}
		return bin; 
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int num=sc.nextInt();
		sc.close();
		String binary=bin(num);
		binary=binary.replaceAll("0", "");
		System.out.println(binary.length());
	}

}
