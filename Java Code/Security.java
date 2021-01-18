package Challenge;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Security {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        String pw=sc.nextLine();
        Pattern pat =Pattern.compile("T(x)*\\$|\\$(x)*T",Pattern.CASE_INSENSITIVE);
        Matcher mat=pat.matcher(pw);
        if (mat.find()) System.out.println("ALARM");
        else System.out.println("quiet");
        sc.close();
    }
}
