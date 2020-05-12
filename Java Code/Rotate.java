import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Rotate {
	static List<String> list;
	static int n;
	static int[][] mat;
	static void InitMatrix() {
		
	}
	public static void main(String[] args) {
		System.out.print("Matrix Size: ");
		Scanner sc= new Scanner(System.in);
		String nSt=sc.nextLine();
		n=Integer.parseInt(nSt);
		list=new ArrayList<>();
		for (int l=0;l<n;l++) {
			System.out.print("Row "+ (l+1)+"= ");
			list.add(sc.nextLine());
		}
		sc.close();
//		System.out.print(list);
		InitMatrix();

	}

}
