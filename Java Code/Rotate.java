import java.util.Scanner;

public class Rotate {
    static int size;
    static double OriginX,OriginY;
    static int[][] mat,matRot90,matRot270;
    static void PrintMatrix(int[][] matrix ) {
        for (int i =0;i<size;i++) {
            System.out.print("ROW "+(i+1)+": ");
            for (int j =0;j<size;j++) {
                System.out.print(matrix[i][j]+ " ");
            }
            System.out.println();
        }
    }
    static void RotateMatrix(int angle ) {
    	int x,y;
    	double x0,y0,fx,fy;
    	switch(angle) {
	    	case 270:
	    		break;
	    	default: //[0,2]
	    		for (int i=0;i<size;i++) {
	    			for(int j=0;j<size;j++) {
	    				x0=i-OriginX; // 0-1=-1
	    				y0=j-OriginY; // 2-1=1
	    				fx=-y0; //-1
	    				fy=x0; // -1
	    				x=(int) (fx+OriginX); //0
	    				y= (int) (fy+OriginY); //0
	    				matRot90[x][y]=mat[i][j];
	    			}
	    		}
    	
    	}
    }
    static void Init(String size_) {
    	size=Integer.parseInt(size_);
        mat=new int[size][size];
        matRot90=new int[size][size];
        matRot270=new int[size][size];
        if (size % 2 == 0 ) {
        	OriginX=size /2;
        	OriginY=size/2;
        }else {
        	OriginX=(size-1) /2 +1;
        	OriginY=(size-1) /2 +1;
        }
    }
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
        PrintMatrix(mat);
        RotateMatrix(90);
        PrintMatrix(matRot90);
        
    }

}
