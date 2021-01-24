using System;
using System.Collections.Generic;
using System.Linq;

namespace It_s_a_sign
{
    
    class Program
    {
        static Boolean isPanlindrome(string str)
        {
            char[] chs = str.ToCharArray();
            Array.Reverse(chs);
            string chk_str = string.Concat(chs);
            return chk_str == str;
        }
        static void Main(string[] args)
        {
            string[] words = new string[4];
            int i=0;
            Boolean result=false;
            for (; i < 4; i++)
            {
                words[i]=Console.ReadLine().ToLower();
            }
            i = 0;
            do
            {
                result = isPanlindrome(words[i]);
                i++;
            } while (!result && i <4 );
            Console.WriteLine(result?"Open":"Trash");
        }
    }
}
