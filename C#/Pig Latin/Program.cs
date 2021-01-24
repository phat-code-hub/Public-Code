using System;
using System.Collections.Generic;

namespace Pig_Latin
{
    class Program
    {
        static void Main(string[] args)
        {
            String[] words = Console.ReadLine().Trim().Split();
            if( !String.IsNullOrEmpty(words[0]))
            {
                List<String> list =new List<string>();
                foreach (string st in words)
                {
                    list.Add( st.Substring(1) + st[0] + "ay");
                }
                Console.WriteLine(String.Join(" ", list));
            }
            else
            {
                Console.WriteLine("Invalid");
            }
        }
    }
}
