using System;
using System.Threading;

namespace Collatz_Conjenture
{
    
    class Program
    {
        static int step=1;
        static void analyse(int number)
        {
            int after;
            int before = number;
            string op_text = "";
            do
            {
                if (before % 2 == 0)
                {
                    after = before / 2;
                    op_text = "/2";
                }
                else
                {
                    after = before * 3 + 1;
                    op_text = "* 3 + 1";
                }
                Console.WriteLine("Step {0}: {1} {2} = {3}", step++, before, op_text, after);
                before = after;
            } while (before > 1);
            Console.WriteLine("After {0} steps , number [{1}] converged to 1", --step, number);
        }
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            if(input.Length>0)
            {
                int num = Convert.ToInt32(input);
                Console.WriteLine();
                analyse(num);
            }
        }
    }
}
