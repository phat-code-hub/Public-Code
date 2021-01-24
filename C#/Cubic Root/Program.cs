using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;

namespace Cubic_Root
{
    class Program
    {
        static string num_;// input number as string type
        static string calc_num_str;// convert to pure real number as string type to calculate
        static bool num_sign; // 1: positive , 0: nagative
        static bool exp_sign; // 1 : positive exponent,0: negative
        static double num;
        //------------------------------------------------------------
        //Analyse input text , convert to calculating corespondent real number
        static void Main(string[] args)
        {
            num_ = Console.ReadLine().Trim();
            try
            {
                char[] chs = num_.ToCharArray();
                HashSet<char> set = new HashSet<char>();
                foreach(char ch in chs)
                {
                    set.Add(ch);
                }
                Console.WriteLine(set.ToArray()+set.ToArray().Length.ToString());
                //num = Convert.ToDouble(num_);
                //Console.WriteLine(num);

            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            
        }
    }
}
