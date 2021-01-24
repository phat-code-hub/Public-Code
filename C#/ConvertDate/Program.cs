using System;
using System.Globalization;

namespace ConvertDate
{
    class Program
    {
        static void Main(string[] args)
        {
             
            string date_str = Console.ReadLine();
            try
            {
                // Convert string to  US format Date
                CultureInfo us_info = new CultureInfo("en-US");
                DateTime date = DateTime.Parse(date_str,us_info);
                //Output to EU format
                Console.WriteLine(date.ToString("d/M/yyyy"));
            } catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            
        }
    }
}
