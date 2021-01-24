using System;
using System.Linq;
using System.Threading.Channels;
using System.Text.RegularExpressions;

namespace Deja_Vu
{
    class Program
    {
        //Deja Vu check Function : note checking condition is case sensitive
        static void isDejaVu(string text)
        {
            char[] chs = text.Trim().ToCharArray();
            string ans = "Unique"; // default : non_repeatable text
            int cnt = 0; // checking standard letter index
            int i = 1;
            do
            {
                //if standard letter is repeated , stop and break checking
                if (chs[cnt].Equals(chs[i]))
                {
                    ans = "Deja Vu";
                    break;
                }
                else
                {
                    if (i == chs.Count()-1) // arrived at last text
                    {
                        //if checking standard letter is still remain
                        cnt++;
                        i = cnt + 1;
                    } else // Checking until last letter
                    {
                        i++;
                    }
                }
            } while (cnt < chs.Count() - 1);
            Console.WriteLine(ans);
        }
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            // Check whether text contains numbers or control char
            Regex reg = new Regex(@"\d+|\s");
            bool m = reg.IsMatch(str.Trim());
            if (m) // invalid text
            {
                Console.WriteLine("Invalid");
            } else // invalid input text
            {
                isDejaVu(str);
            }
        }
    }
}
