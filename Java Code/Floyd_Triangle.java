import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Floyd_Triangle {
	static List<Integer> list;
	static List<Integer> rev_List;
	//Find the max number to display
	private static int lastNumber(int n) {
		if (n==1){
			return 1;
		} else {
			return lastNumber(n-1)+n;
		}
	}
	//Prepare list to show
	private static void makeList(int rows) {
		int max_number=lastNumber(rows);
		list=Stream.iterate(1, n-> n+1)
				.limit(max_number)
				.collect(Collectors.toList());
		//make reversed list number to show 
		rev_List=list.stream().sorted((n1,n2)->n2-n1).collect(Collectors.toList());
	}
	static void display(int rows) {
		int count=0;
		System.out.println();
		System.out.println("Floyd Triangle:");
		for (int row=1; row<=rows;row++) {
			for (int ord=0;ord<row;ord++) {
				System.out.print(list.get(count)+" ");
				count++;
			}
			System.out.println();
		}
		count=0;
		System.out.println();
		System.out.println("Reversed Floyd Triangle:");
		for (int row=1; row<=rows;row++) {
			for (int ord=0;ord<rows-row+1;ord++) {
				System.out.print(rev_List.get(count)+" ");
				count++;
			}
			System.out.println();
		}
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.print("How many rows (>0) to display: ");
		try {
			int row_num=sc.nextInt();
			if (row_num > 0){
				makeList(row_num);
				display(row_num);
			}else {
				System.out.println("Row must be positive!");
			}
		}catch (Exception e) {
			System.out.println("Invalid Number");
		}finally {
			sc.close();
		}
	}

}
