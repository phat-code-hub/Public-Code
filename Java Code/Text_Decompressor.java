import java.util.Scanner;
public class Text_Decompressor {
	static StringBuilder ReplaceSt(StringBuilder stbl , int times) {
		String DecompressedChar=stbl.substring(stbl.length()-1);
		stbl=stbl.deleteCharAt(stbl.length()-1);
		for (int j=0;j<times;j++) {
			stbl.append(DecompressedChar);
		}
		return stbl;
	}
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		try {
			String st=sc.nextLine();
			StringBuilder stb=new StringBuilder();
			for (int i=0; i<st.length();i++) {
				char  c=st.charAt(i);
				if (!(c>='0' && c<='9')) {
					stb.append(c);
				}else {
					stb=ReplaceSt(stb,Integer.parseInt(String.valueOf(c)));
				}	
			}
			System.out.println(stb);		
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		finally {
			sc.close();
		}

	}

}
