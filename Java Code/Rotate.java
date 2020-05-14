import java.util.Scanner;

public class Rotate {
    static int size;
    static double OriginX,OriginY;
    static int[][] mat,matRot90,matRot270;
  //---------------------------------------------------
    static void PrintMatrix(int[][] matrix ) {
        for (int i =0;i<size;i++) {
            for (int j =0;j<size;j++) {
                System.out.print(matrix[i][j]+ " ");
            }
            System.out.println();
        }
    }
  //---------------------------------------------------
    static void RotateMatrix(int angle ) {
    	int x,y;
    	double x0,y0,fx,fy;
    	int signX,signY;
    	int[][] tempMat=new int[size][size];
    	signX=(angle == 90) ? -1:1;
    	signY=(angle == 270) ? -1:1;
    	for (int i=0;i<size;i++) {
			for(int j=0;j<size;j++) {
				x0=i-OriginX; 
				y0=j-OriginY; 
				fx=signX*y0; 
				fy=signY*x0; 
				x=(int) (fx+OriginX); 
				y= (int) (fy+OriginY);
				tempMat[x][y]=mat[i][j];
			}
		}
    	if (angle ==270) matRot270= tempMat;
    	else matRot90=tempMat;
    }
  //---------------------------------------------------
    static void Init(String size_) {
    	size=Integer.parseInt(size_);
        mat=new int[size][size];
        matRot90=new int[size][size];
        matRot270=new int[size][size];
        if (size % 2 == 0 ) {
        	OriginX=(double) (size-1) /2;
        	OriginY=(double) (size-1)/2;
        }else {
        	OriginX=(double) (size-1) /2 ;
        	OriginY=(double) (size-1) /2 ;
        }
        
    }
  //---------------------------------------------------
    static void InitRow(int idx,String nums ) {
        nums=nums.trim();
        String[] rows=nums.split("[\\s,]+");
        for (int j=0;j<size;j++) {
            mat[idx][j]=Integer.parseInt(rows[j]);
        }
    }
//---------------------------------------------------
    public static void main(String[] args) {
        System.out.print("Matrix Size: ");
        Scanner sc= new Scanner(System.in);
        String nSt=sc.nextLine();
        Init(nSt);
        for (int l=0;l<size;l++) {
            System.out.print("Row "+ (l+1)+"= ");
            String row=sc.nextLine();
            InitRow(l,row);
        }
        sc.close();
        System.out.println("Origin Martrix:");
        PrintMatrix(mat);
        System.out.println("Rotate 90 degrees:");
        RotateMatrix(90);
        PrintMatrix(matRot90);
        System.out.println("Rotate 270 degrees:");
        RotateMatrix(270);
        PrintMatrix(matRot270);
    }

}
