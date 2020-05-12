import java.util.*;

public class Rotate_Matrix {
	public static int[][] mat;
	public static int N;
	static void InitMatrix (int idx,String str)  {
		String[] sts=str.trim().split("[\\s,]+");
		mat[idx] =new int[N];
		for (int j=0; j<N;j++) {
			mat[idx][j]=Integer.parseInt(sts[j]);
		}
	}

	public static void main(String[] args) {
<<<<<<< HEAD
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
=======
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

>>>>>>> 299d6b876dbf2cac11b90ca7e6c7487e21e9ed65
	}

}
