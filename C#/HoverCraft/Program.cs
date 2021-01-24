using System;

namespace HoverCraft
{
    class Program
    {
        static void Main(string[] args)
        {
            const int PRICE = 3_000_000;
            const int INSURANCE = 1_000_000;
            const int MONTHLY_CAPACITY = 10;
            const int UNIT_COST = 2_000_000;
            int customer = Convert.ToInt32(Console.ReadLine());
            int expence = MONTHLY_CAPACITY * UNIT_COST + INSURANCE;
            int income = customer * PRICE;
            if (income > expence) Console.WriteLine("Profit");
            else if (income == expence) Console.WriteLine("Broken Even");
            else Console.WriteLine("Loss");
        }
    }
}
