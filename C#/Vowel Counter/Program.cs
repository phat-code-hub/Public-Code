using System;
using System.Linq;

namespace Vowel_Counter
{   
    
    class Program
    {   
        const string VOWEL = "AIUEOaiueo";
        static void Main(string[] args)
        {
            string text = Console.ReadLine().Trim();
            if (text.Length > 0)
            {
                int count = 0;
                char[] chs = text.ToCharArray();
                foreach (char c in chs)
                {
                    if (VOWEL.Contains(c))
                    {
                        count++;
                    }
                }
                Console.WriteLine(count);
            }
            else Console.WriteLine(text.Length);
        }
    }
}
