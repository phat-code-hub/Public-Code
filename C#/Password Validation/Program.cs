using System;
using System.Text;
using System.Text.RegularExpressions;

namespace Password_Validation
{
    class Program
    {   
        // Check text has special character or not
        static String isSpecialChar(string word)
        {
            char[] chars = word.ToCharArray();
            foreach(char c in chars)
            {
                if (!(char.IsLetterOrDigit(c))) return "true";
            }
            return "false";
        }
        //------------------------------------------------
        // Check text has numeric number and no space
        static string isValid(string str)
        {
            Regex regex;
            bool matche;
            //Check at least one number
            regex = new Regex(@"\d+");
            matche = regex.IsMatch(str);
            if (!matche) return "false";
            else
            {
                //check no space
                regex = new Regex(@"\s+");
                matche = regex.IsMatch(str);
                if (matche) return "false";
                // Check special Character
                else return isSpecialChar(str);
            }
        }
        //------------------------------------------------
        //main code
        static void Main(string[] args)
        {
            string answer = "true";
            string text= Console.ReadLine().Trim();
            if (text.Length >= 5 && text.Length <= 10) answer = isValid(text);
            else answer="false";
            Console.WriteLine(answer);
        }
    }
}
