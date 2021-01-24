using System;

namespace RemoveSpaceFromString
{
    class Program
    {
        static void Main(string[] args)
        {
            string inputStr = Console.ReadLine().Trim();
            string outputStr = inputStr.Replace(" ", "");
            Console.WriteLine(outputStr);

        }
    }
}
