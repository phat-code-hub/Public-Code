import java.util.*;
import java.util.Scanner;

public class Gapful_Numbers {
	static int  min,max;
	//Check one number
	static boolean isGapful(int num) {
		String str=String.valueOf(num);
		int num2=Integer.parseInt(str.substring(0,1)+str.substring(str.length()-1));
		return ((num % num2) == 0 )? true:false;
	}
	//Find Gapful numbers in range 
	static void findNumbers(int min,int max)  {
		List<Integer> found =new ArrayList<>() ;
		for (int n=min;n<=max;n++) {
			if(isGapful(n)) {
				found.add(n);
			}
		}
		System.out.println();
		if (found.size() >0) {
			System.out.printf("In range [%d,%d] , there are %d Gapful numbers:\n",min,max,found.size());
			//System.out.println(found); // print with format []
			found.stream()
				.forEach(s-> System.out.print(s+ " "));
		}else 
			System.out.println("There is no any gapful numbers in this range!");
	}
	//main code
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("0: Check one gapful number.");
		System.out.println("1: Find gapful numbers from range.");
		System.out.print("Chose option :");
		try {
			int opt=sc.nextInt();
			if (opt==0) {
				System.out.print("Enter number (>99) :");
				int num=sc.nextInt();
				if (num>99 ) {
					System.out.println(isGapful(num));
				} else {
					System.out.println("Number invalid (<100)!");
					throw new Exception();
				}
			} else if (opt ==1) {
				System.out.print("Enter range (min,max) with min >99 :");
				String find_range= sc.next();
				String[] limit=find_range.split(",");
				int down=Integer.parseInt(limit[0]);
				int up=Integer.parseInt(limit[1]);
				if (up <down) {
					int temp=down;
					down=up;
					up=temp;
				}
				if (down >99  ) findNumbers(down,up);
				else {
					System.out.println("Invalid range (min <100)!");
					throw new Exception();
				}
			}else {
				System.out.println("Option must be 0 or 1!");
				throw new Exception();
			}
		}catch (Exception e) {
			e.printStackTrace();
		}finally {
			sc.close();
		}

	}

}
