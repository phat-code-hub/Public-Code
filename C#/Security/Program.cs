using System;
using System.Text.RegularExpressions;
namespace Security
{
    class Program
    {
        static void Main(string[] args)
        {
            string pw = Console.ReadLine().Trim();
            var reg = new Regex(@"\$(x)*T|T(x)*\$", RegexOptions.IgnoreCase);
            if (reg.IsMatch(pw)) Console.WriteLine("ALARM");
            else Console.WriteLine("quiet");

        }
    }
}
