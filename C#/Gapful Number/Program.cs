using System;
using System.IO.Pipes;
using System.Linq;
using System.Collections.Generic;

namespace Gapful_Number
{
   
    class Program
    {
        static int option = -1;
        static List<int> result;
        //-----------------------------------------------
        static void MainMenu()
        {
            Console.WriteLine("Gapful Number Check: ");
            Console.WriteLine("  0:Check one number.");
            Console.WriteLine("  1:List up numbers in range.");
            Console.Write("Choice Option: ");
            String opt = Console.ReadLine();
            if (Convert.ToInt32(opt) < 2) option = Convert.ToInt32(opt);
        }
        //-----------------------------------------------
        static bool isGapful(int number)
        {
            string st_num = number.ToString();
            string no_str = st_num.Substring(0, 1) + st_num.Substring(st_num.Length - 1, 1);
            int no = Convert.ToInt32(no_str);
            return (number % no) == 0;
        }
        //-----------------------------------------------
        static void listUp(string lim1, string lim2)
        {
            result = new List<int>();
            int min = Convert.ToInt32(lim1);
            int max = Convert.ToInt32(lim2);
            if (min>max)
            {
                int temp = min;
                min = max;
                max = temp;
            }
            for (int n = min; n <= max; n++)
            {
                if (isGapful(n)==true)
                {
                    result.Add(n);
                } 
            }
            if (result.Count > 0)
            {
                Console.WriteLine("There are {0} gapful numbers in range [{1}-{2}]:",
                    result.Count, min, max);
                Console.WriteLine(string.Join(" ", result));
            }
            else
            {
                Console.WriteLine("There was no any gapful numbers in given range!");
            }
        }
        //-----------------------------------------------
        static void Menu1()
        {
            Console.Write("Input number (>99): ");
            String num0 = Console.ReadLine();
            int num = Convert.ToInt32(num0);
            if (num >= 100)
            {
                Console.WriteLine(isGapful(num) ? "true" : "false");
            }
            else
            {
                Console.WriteLine("{0} <100!", num);
            }
        }
        //-----------------------------------------------
        static void Menu2()
        {
            string down, up;
            Console.Write("Min limit(>99):");
            down= Console.ReadLine();
            Console.Write("Max limit(>min): ");
            up=Console.ReadLine();
            if (Convert.ToInt32(down) >99)
            {
                listUp(down, up);
            } else
            {
                Console.WriteLine("{0} < 100 : Invalid");
            }
            
        }
        //-----------------------------------------------
        static void Main(string[] args)
        {
            MainMenu();
            switch (option)
            {
                case 0:
                    Menu1();
                    break;
                case 1:
                    Menu2();
                    break;
                default:
                    break;
            }
            
        }
       
    }
}
