using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Schema;

namespace Summations_Calculator
{
    class Program
    {
        static int min, max, num;
        static char oper;
        static int total ;
        static List<string> lst;
        //-----------------------------------------------------------
        //assign to variable 
        static void analyse(string[] express)
        {   min = Convert.ToInt32(express[0]);
            max = Convert.ToInt32(express[1]);
            oper = char.Parse(express[2].Substring(0, 1));
            num = Convert.ToInt32(express[2].Substring(1));
        }
        //-----------------------------------------------------------
        //Combine all calculate results to list
        static void listUp(int number,char op)
        {
            lst.Add(number.ToString() + op.ToString() + num.ToString());
        }
        //-----------------------------------------------------------
        //Calculate Total
        static void calculate()
        {
            lst = new List<string>();
            total = 0;
            for(int i = Math.Min(min, max); i <= Math.Max(min,max); i++)
            {
                switch (oper)
                {
                    case '+':
                        {
                            total += i+num;
                            break;
                        }
                    case '-':
                        {
                            total += i-num;
                            break;
                        }
                    case '/':
                        {
                            total += i/num;
                            break;
                        }
                    case '%':
                        {
                            total += i%num;
                            break;
                        }
                    default: 
                        {
                            total += i*num;
                            break;
                        }

                }
                listUp(i, oper);
            }
            String res = string.Join(" + ", lst.ToArray());
            Console.WriteLine("{0} ({1})", total,res);
        }
        //-----------------------------------------------------------
        //Main Code
        static void Main(string[] args)
        {
            string word = Console.ReadLine().Trim();
            string[] text = word.Split(" ");
            try
            {
                analyse(text);
                calculate();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }
    }
}
