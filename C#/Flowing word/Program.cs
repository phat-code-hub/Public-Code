using System;

namespace Flowing_word
{
    class Program
    {
        static string[] words;
        static string ChkFlowing(string[] wd)
        {
            char last = char.Parse(wd[0].Substring(wd[0].Length-1));
            char first= char.Parse(wd[1].Substring(0, 1));
            int i = 1;  
            do
            {
                if (!last.Equals(first)) {
                    return "false";
                } else
                {
                    if (i!=wd.Length-1)
                    {
                        last = char.Parse(wd[i].Substring(wd[i].Length - 1));
                        first = char.Parse(wd[++i].Substring(0, 1));
                    }
                }

            } while (i < wd.Length-1);

            return("true");
        }
        static void Main(string[] args)
        {
            words = Console.ReadLine().ToLower().Split();
            if (words.Length > 1) {
                Console.WriteLine(ChkFlowing(words));
            }else
            {
                Console.WriteLine("false");
            }

        }
    }
}
