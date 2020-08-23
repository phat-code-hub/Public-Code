import java.util.Scanner;

public class Extra_Terrestrials {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		try {
			String st=sc.nextLine();
			StringBuilder str=new StringBuilder(st);
			System.out.println(str.reverse());
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		finally {
			sc.close();
		}
	}

}
