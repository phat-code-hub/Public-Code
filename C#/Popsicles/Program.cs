using System;

namespace Popsicles
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                string[] data = Console.ReadLine().Trim().Split();
                int siblings = Convert.ToInt32(data[0]);
                int popsicles = Convert.ToInt32(data[1]);
                //calculate division of  two data
                if (popsicles % siblings == 0) Console.WriteLine("give away");
                else Console.WriteLine("eat them yourself");

            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }
    }
}
