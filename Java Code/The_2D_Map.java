import java.util.Scanner;
class Index {
	private int i;
	private int j;
	public Index(int i, int j) {
		this.i = i;
		this.j = j;
	}
	public int getI() {
		return i;
	}
	public void setI(int i) {
		this.i = i;
	}
	public int getJ() {
		return j;
	}
	public void setJ(int j) {
		this.j = j;
	}
	public static int totalMoves(Index p1,Index p2) {
		int hmove=Math.abs(p2.getJ()-p1.getJ());
		int vmove=Math.abs(p2.getI()-p1.getI());
		return hmove+vmove;
	}
}
public class The_2D_Map {

	public static void main(String[] args) {
		try {
			char key='P';
			System.out.print("2D Array: ");
			Scanner sc=new Scanner(System.in);
			String map_=sc.nextLine().trim();
			sc.close();
			String[] map=map_.split(",");
			Index firstP=new Index(0,0);
			Index secondP=new Index(0,0);
			boolean isP1=false;
			boolean isP2=false;
			for (int i=0;i<5;i++) {
				String st=map[i];
				for (int j=0; j<st.length();j++) {
					if(st.charAt(j)==key) {
						if (!isP1) {
							firstP.setI(i);
							firstP.setJ(j);
							isP1=true;
						}
						else if(isP1 & !isP2) {
							secondP.setI(i);
							secondP.setJ(j);
							isP2=true;
						}
					}
				}
			}
			if (isP1 & isP2) System.out.println(Index.totalMoves(firstP, secondP));
			else System.out.println(0);
		}catch(Exception e) {
			e.printStackTrace();
		}
	}

}
