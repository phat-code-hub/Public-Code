using System;

namespace MilitaryTime
{
    class Program
    {
        static void Main(string[] args)
        {
            string dt_str = Console.ReadLine();
            DateTime dt = DateTime.Parse(dt_str);
            Console.WriteLine(dt.ToShortTimeString());
        }
    }
}
