using System;

namespace Cheer_Creator
{
    class Program
    {
        static void Main(string[] args)
        {
            int yard = Convert.ToInt32(Console.ReadLine());
            if (yard > 10) Console.WriteLine("High Five");
            else if (yard < 1) Console.WriteLine("shh");
            else
            {
                String sound = "";
                for (int n =0; n < yard; n++)
                {
                    sound += "Ra!";
                };
                Console.WriteLine(sound);
            }
        }
    }
}
