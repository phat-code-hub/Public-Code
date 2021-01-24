using System;
using System.Runtime.InteropServices;

namespace Day_of_the_week
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime dt;
            string strtime = "";
            string format1 = "M/d/yyyy";
            string format2 = "MMMM d, yyyy";
            string format = "";
            try
            {
                strtime = Console.ReadLine().Trim();
                if(strtime.Contains("/"))
                {
                    format = format1;
                }
                else {
                    format = format2;
                }
                dt = DateTime.ParseExact(strtime, format, null);
                Console.WriteLine(dt.ToString("dddd"));
            } catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            
        }
    }
}
