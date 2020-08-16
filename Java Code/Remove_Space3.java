import java.util.*;
import java.util.Scanner;

public class Remove_Space3 {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		System.out.print("String: ");
		String string=sc.nextLine();
		sc.close();
		String[] array=string.split(" ");
		List<String> list=new ArrayList<>();
		for (String st : array) {
			if (st != " "){
				list.add(st);
			}
		}
		String result=String.join("", list);
		System.out.println("After remove spaces :"+ result);

	}

}
