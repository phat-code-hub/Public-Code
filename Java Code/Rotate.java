import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Rotate {

	public static void main(String[] args) {
		System.out.print("Matrix Size: ");
		Scanner sc= new Scanner(System.in);
		String Nst=sc.nextLine();
		int N=Integer.parseInt(Nst);
		List<String> list=new ArrayList<>();
		for (int l=0;l<N;l++) {
			System.out.print("Row "+ (l+1)+"= ");
			list.add(sc.nextLine());
		}
		sc.close();
		System.out.print(list);

	}

}
