import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.function.BinaryOperator;

public class Summations_Calculator {
	static int min,max,value;
	static String oper;
	//Split input content
	static void analyse(String st) throws Exception{
		try {
			String[] temp=st.split(" ");
			if (temp.length == 3) {
				min=Integer.parseInt(temp[0]);
				max=Integer.parseInt(temp[1]);
				if (min>max) {
					min=min*max;
					max=min/max;
					min=min/max;
				}
				oper=temp[2].substring(0,1);
				value=Integer.parseInt(temp[2].substring(1));
				summations();
			} else throw new Exception();
		}catch(Exception e) {
			System.out.println("Can not find 3 elements!");
			throw new Exception();
		}
	}
	//Calculate
	static void summations() {
		BinaryOperator<Integer> f=null;
		switch (oper) {
		case "+":
			f=(n1,n2) -> n1+n2;
			break;
		case "-":
			f=(n1,n2) -> n1-n2;
			break;
		case "x":
		case "X":
		case "*":
			f=(n1,n2) -> n1*n2;
			break;
		case "/":
			f=(n1,n2) -> n1/n2;
			break;
		case "%":
			f=(n1,n2) -> n1%n2;
			break;
		};
		List<String> expr=new ArrayList<>();
		int total=0;
		for (int i=min; i<=max;i++) {
			total += f.apply(i, value);
			expr.add(i+oper.toLowerCase()+value);
		}
		System.out.println(total+" ("+String.join("+",expr)+")");
	}
	public static void main(String[] args) {
		String input;
		Scanner sc =new Scanner(System.in);
		try {
			input=sc.nextLine();
			if (input.trim().length()>0) {
				analyse(input);
			} else {
				System.out.println("Invalid content!");
			}
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			sc.close();
		}
	}

}
