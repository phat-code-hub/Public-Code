import java.util.*;

public class Rotate_Matrix {
	public static int[][] mat;
	public static int N;
	static void InitMatrix (int idx,String str)  {
		String[] sts=str.trim().split("[\\s,]+");
		mat[idx] =new int[N];
		for (int j=0; j<N;j++) {
		}
	}

	public static void main(String[] args) {
		int nums=0;
		System.out.print("Matrix Size N = ");
		Scanner sc= new Scanner(System.in);
		N= sc.nextInt();
		List<List<String>> list=new ArrayList<>();
		while( sc.hasNextLine()) {
			List<String> token=new ArrayList<>();
			Scanner newsc= new Scanner(sc.nextLine());
			while(newsc.hasNext()) {
				token.add(newsc.next());
				list.add(token);
			}
			newsc.close();
			
		}
		
		sc.close();
		System.out.println(list);
//		for (int i =0; i<N;i++) {
//			for (int j=0;j<N; j++) {
//				System.out.print(mat[i][j] + " ");
//			}
//			System.out.println();
//		}

	}

}
