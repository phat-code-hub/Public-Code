import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Day_of_the_Week {
	public static void main(String[] args) {
		try {
			SimpleDateFormat inputDate=new SimpleDateFormat("MM/dd/yyyy");
			System.out.print("Date :");
			Scanner sc=new Scanner(System.in);
			String inputdate=sc.nextLine().trim();
			sc.close();
			if (inputdate.contains(",")) {
				inputDate=new SimpleDateFormat("MMMM dd, yyyy");
			}
			Date date=inputDate.parse(inputdate);
			SimpleDateFormat outputWeek=new SimpleDateFormat("EEEE");
			System.out.println(outputWeek.format(date));
		}
		catch (Exception e) {
			e.printStackTrace();
		}
	}

}
