import java.util.*;
import java.util.stream.*;

public class Missing_Numbers {
	static void Analyse(List<Integer> lst) {
		List<Integer> lack_num= new ArrayList<>();
		for (int j=lst.get(0); j<=lst.get(lst.size()-1); j++) {
			if (! lst.contains(j) ) {
				lack_num.add(j);
			}
		}
		lack_num.stream()
			.forEach(n-> System.out.print(n+ " "));
	}
	public static void main(String[] args) {
		List<Integer> list= new ArrayList<>();
		Scanner sc= new Scanner(System.in);
		System.out.print("N= ");
		int n= sc.nextInt();
		System.out.println("Input Numbers: ");
		String st="";
		for (int i =0; i<n; i++) {
			st=sc.next();
			if (st !="") {
				list.add(Integer.parseInt(st));
			}
		}
		sc.close();
		list=list.stream()
			.sorted()
		    .collect(Collectors.toList());
		Analyse(list);
	}

}
