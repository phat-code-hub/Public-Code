package Challenge;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class ConvertDate {
    //Change Format Date
    static void Format_US_to_EU(String date_str){
        //Formatted Pattern of EU Date 
        DateTimeFormatter EU_output=DateTimeFormatter.ofPattern("d/M/yyyy");
        //Formatted Pattern of input US Date depends 2 types
        DateTimeFormatter US_input=null;
        if (date_str.contains("/")){
            US_input=DateTimeFormatter.ofPattern("M/d/y",Locale.ENGLISH);
        } else{
            US_input=DateTimeFormatter.ofPattern("MMMM d, y",Locale.ENGLISH);
        }
        //Convert input String to formatted pattern Date
        LocalDate date=LocalDate.parse(date_str,US_input); 
        //Output Date with EUformat
        System.out.println(EU_output.format(date));
    }
    //Main Code
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        try {
            Format_US_to_EU(sc.nextLine().trim());
        }finally {
            sc.close();
        }
    } 
}
