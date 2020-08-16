import java.util.Scanner;
import java.util.stream.Stream;

public class Multiples {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		sc.close();
		Stream<Integer> st=Stream.iterate(3, i-> ++i);
		int sum= st.limit(n-3)
				.filter(p-> (p % 3 ==0 || p % 5 == 0))
				.reduce(0, (n1,n2) -> n1+n2);
		System.out.println(sum);
	}
}
