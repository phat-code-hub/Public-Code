using System;

namespace Hex_Color_Code_Generator
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] Color = new string[3];
            for(var i = 0; i < 3; i++)
            {
                Color[i] = Console.ReadLine();

            }
            int num=0;
            Console.Write("#");
            foreach(string st in Color)
            {
                num = Convert.ToInt32(st);
                Console.Write(num.ToString("X").ToLower());

            }
        }
    }
}
    