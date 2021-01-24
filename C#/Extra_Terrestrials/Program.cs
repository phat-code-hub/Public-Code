using System;
using System.Linq;

namespace Extra_Terrestrials
{
    class Program
    {
        static string Reverse(string st)
        {
            if (st == null) return "";
            char[] c = st.ToCharArray();
            Array.Reverse(c);
            return new string(c);
        }
        static void Main(string[] args)
        {
            string word = Console.ReadLine().Trim();
            Console.WriteLine(Reverse(word));
        }
    }
}
