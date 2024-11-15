import java.util.Scanner;
// import java.util.stream.IntStream;

public class Spiral_Matrix_2 {
    public static void main(String[] args) {
        int N=0;
        Scanner sc= new Scanner(System.in);
        N = sc.nextInt();
        int[][] arr = new int[N][N];
        sc.close();
        int cnt =1;
        // Khoi tao
        for (int[] ar:arr){
            for (int a: ar){
                a=0;
            }
        }
        for (var loop=0;loop<(N+1)/2;loop++){
            // direction 1 - traverse from left to right
            for (int i=loop;i<(N-loop);i++ ) arr[loop][i] = cnt++;
            // direction 2 - traverse from top to bottom
            for (int i=loop+1;i<(N-loop);i++ ) arr[i][N-loop-1] = cnt++;
            // direction 3 - traverse from right to left
            for (int i=N-loop-2;i>(loop-1);i-- ) arr[N-loop-1][i] = cnt++;
            // direction 4 - traverse from bottom to top
            for (int i=N-loop-2;i>(loop);i-- ) arr[i][loop] = cnt++;
        }

        for (int[] ar:arr){
            for (int a: ar){
                System.out.print(a+"  ");
            }
            System.out.println();
        }
    }
}
