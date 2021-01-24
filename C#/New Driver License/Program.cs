using System;
using System.Collections.Generic;

namespace New_Driver_License
{
    class Program
    {
        const int WAITTING_TIME = 20;
        static void Main(string[] args)
        {

            List<String> peoples = new List<string>();
            string name = Console.ReadLine();
            int agents = Convert.ToInt32(Console.ReadLine());
            string[] group = Console.ReadLine().Trim().Split(" ");
            peoples.AddRange(group);
            peoples.Add(name);
            peoples.Sort();
            int my_order = peoples.IndexOf(name);
            int my_group = my_order / agents;
            Console.WriteLine((my_group+1)*WAITTING_TIME);
        }
    }
}
