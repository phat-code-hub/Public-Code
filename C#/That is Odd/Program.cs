using System;
using System.Collections.Generic;
using System.Linq;

namespace That_is_Odd
{
    class Program
    {
        private static bool isEven(int num)
        {
            return num % 2 == 0;
        }
        static void Main(string[] args)
        {
            List<int> lst = new List<int>();
            int num = Convert.ToInt32(Console.ReadLine());
            for (int i = 0; i < num; i++)
            {
                lst.Add(Convert.ToInt32(Console.ReadLine()));
            }
            List<int> even_List = lst.FindAll(isEven);
            Console.WriteLine(even_List.Sum());
        }
    }
}
