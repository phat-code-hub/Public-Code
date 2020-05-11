import java.util.*;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Rotate_Matrix {

	public static void main(String[] args) {
		System.out.print("Chuoi: ");
		Scanner sc= new Scanner(System.in);
		String st= sc.nextLine();
		sc.close();
		String[] sts=st.trim().split("[\\s,]+");
		List<List<Integer>> rows=new ArrayList<>();
		List<Integer> strs=Stream.of(sts)
				.map(n -> Integer.parseInt(n))
				.collect(Collectors.toList());
		rows.add(Arrays.asList(1,2,3,4));
		rows.add(strs);	
		rows.stream().forEach(s -> System.out.println(s));
	}

}
