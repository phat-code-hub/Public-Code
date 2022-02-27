using System;
using System.Globalization;

namespace Day_Between_Dates
{
    class Program
    {
        static void Main(string[] args)
        {
            var st1 = Console.ReadLine();
            var st2 = Console.ReadLine();
            var format = "MMMM dd, yyyy";
            //var dts = DateTimeStyles.AssumeUniversal;
            CultureInfo culture = new CultureInfo("en-US");
            DateTime dt1 = DateTime.ParseExact(st1, format, culture);
            DateTime dt2 = DateTime.ParseExact(st2, format, culture);
            //var ans = dt1 - dt2;
            var ans = dt2.Subtract(dt1);
            //Console.WriteLine(ans.ToString("%d"));
            Console.WriteLine(ans.Days);
        }
    }
}
