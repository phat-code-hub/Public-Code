using System;

namespace Password_Validation_2
{
    class Program
    {
        static void Main(string[] args)
        {
            const string SPECIAL= "!@#$%&*";
            int sum1 = 0, sum2 = 0;
            string ans = "Weak";
            string words = Console.ReadLine().Trim();
            if (words.Length >=7)
            {
                foreach (char c in words)
                {
                    if (Char.IsNumber(c)) sum1++;
                    if (SPECIAL.Contains(c)) sum2++;
                }
                Console.WriteLine(sum1 + ",,"+sum2);
                ans = (sum1 >= 2 && sum2 >= 2) ? "Strong" : "Weak";

            }
            Console.WriteLine(ans);
            
        }
    }
}
