import java.util.Scanner;
public class Text_Decompressor {
	static String word;
	static char c;
	static StringBuilder num_part=new StringBuilder();
	static StringBuilder char_part=new StringBuilder();
	//-------------------------------------------------------
	//Decompressed character method
	static void Decompressed_Char(boolean isLast ) {
		String temp="";
		int del_index=char_part.length()-1;
		char del_char=char_part.charAt(del_index);
		char_part.deleteCharAt(del_index);
		int replaceTimes=Integer.parseInt(String.valueOf(num_part));
		for (int j=0;j<replaceTimes;j++ ) {
			temp += del_char;
		}
		if (!isLast) {
			temp+=c;
		}
		char_part.replace(del_index,del_index, temp);
		num_part=new StringBuilder();
	}
	//-------------------------------------------------------
	//main code
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		try {
			word=sc.nextLine().trim();
			int i=0;
			//String chars;
			while (i <word.length()) {
				c=word.charAt(i);
				if (c>='0' && c <='9') {
					num_part.append(c);
				}else {
					if (num_part.length()>0) Decompressed_Char(false); // Decompress	
					else char_part.append(c);
				}
				i++;
				//Replace last character if any
				if (i==word.length() && (c>='0' && c<='9')) Decompressed_Char(true);
				
			}
			System.out.println(char_part);
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		finally {
			sc.close();
		}

	}

}
