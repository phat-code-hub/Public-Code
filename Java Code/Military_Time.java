

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class Military_Time {
	static void Convert(String time_string) {
		try {
			//change format of input time
			String lt=LocalTime.parse(time_string,DateTimeFormatter.ofPattern("h:mm a")).
					format(DateTimeFormatter.ofPattern("H:mm"));
			System.out.println(lt);
		}
		catch (Exception e) {
			e.printStackTrace();
		}
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.print("Input time: ");
		String time_str=sc.nextLine();
		sc.close();
		Military_Time.Convert(time_str);
	}

}
