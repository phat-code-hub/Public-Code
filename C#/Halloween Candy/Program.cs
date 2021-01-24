using System;

namespace Halloween_Candy
{
    class Program
    {
        static void Main(string[] args)
        {
            //get visted houses numbers
            int houses = Convert.ToInt32(Console.ReadLine());
            if (houses >= 3)
            {
                //Change  to double by set 2-> 2.0
                double getBillPercentage = (2.0 * 100) / houses;
                //Round the Percentage of getting dollarBill
                Console.WriteLine(Math.Ceiling(getBillPercentage));
            }
            else Console.WriteLine("Visited Houses must be greater than 3!");
            
        }
    }
}
