import java.util.*;

public class Base_Converter {
	static final String BASES="0123456789ABCDEFGHIKLMNOPQRSTUVYWXYZ";
	public static Scanner sc;
	static String Convert(String num_str,String base_str) {
		int num,base;
		int div,mod;
		num=Integer.parseInt(num_str);
		base=Integer.parseInt(base_str);
		String temp_Result="";
		do {
			div = num /base;
			mod=num % base;
			temp_Result=BASES.charAt(mod) + temp_Result;
			num =div;
		} while (num>0);
		return temp_Result;
	}
	public static void main(String[] args) {
		try {
			System.out.print("Input number and base to convert: ");
			sc=new Scanner(System.in);
			String str=sc.nextLine();
			String[] num_base=str.split(" ");
			String num_str=num_base[0];
			String base_str=num_base[1];
			
			if (Integer.parseInt(base_str)==10) {
				System.out.println("This number is not changed!");
			} else {
				String result=Base_Converter.Convert(num_str,base_str);
				System.out.printf("number %s in base %s is %s",num_str,base_str,result);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			sc.close();
		}
	}

}
