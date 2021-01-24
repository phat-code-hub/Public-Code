using System;

namespace BallPark_Order
{
    class Program
    {
        const double TAX = 1.07;
        static double Calc(string st)
        {
            double price=0.0;
            switch (st.ToLower())
            {
                case ("nachos"):
                    price = 6.0;
                    break;
                case ("pizza"):
                    price = 6.0;
                    break;
                case ("cheeseburger"):
                    price = 10.0;
                    break;
                case ("water"):
                    price = 4.0;
                    break;
                
                default:
                    price = 5.0;
                    break;
            }
            return price;
        }
        static void Main(string[] args)
        {
            String[] str = Console.ReadLine().Trim().Split(" ");
            double total = 0.0;
            foreach (string s in str)
            {
                total += Calc(s) ;
            }
            total *= TAX;
            Console.WriteLine(String.Format("{0:0.00}",total));

        }
    }
}
