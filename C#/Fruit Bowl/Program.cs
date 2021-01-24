using System;

namespace Fruit_Bowl
{
    class Program
    {
        static void Main(string[] args)
        {
            int fruit;
            fruit = Convert.ToInt32(Console.ReadLine());
            int apples = (fruit / 2) / 3;
            Console.WriteLine(apples);
        }
    }
}
