using System;

namespace Youtube_Link_Finder
{
    class Program
    {
        static void Main(string[] args)
        {
            string link_ = Console.ReadLine().Trim();
            if (link_.Length > 0)
            {
                string search_pat = "watch?v=";
                int index = link_.IndexOf(search_pat);
                if (index>-1)
                {
                    Console.WriteLine(link_.Substring(index + search_pat.Length));
                } else
                {
                    string[] strs = link_.Split("/");
                    Console.WriteLine(strs[strs.Length-1]);
                }

            }
            
        }
    }
}
