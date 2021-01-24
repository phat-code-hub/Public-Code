using System;
using System.Collections.Generic;
using System.Linq;

namespace AverageWordLength
{
    class Program
    {
        static void Main(string[] args)
        {
            //String words = Console.ReadLine().Trim();
            //List<String> lst = new List<string>();
            //int sum = 0;
            //lst.AddRange(words.Split(" "));
            //lst.ForEach(delegate (String word)
            //{
            //    sum += word.Length;
            //});
            //double avg = (double) sum / (double)lst.Count;
            //Console.WriteLine(avg);
            //if (avg >= 3.5)
            //{
            //    Console.WriteLine(Math.Ceiling(avg));
            //} else
            //{
            //    Console.WriteLine(Math.Round(avg));
            //}
            int[] a = { 10, 15, 16 };
            var b = a.FirstOrDefault(
                 z => z.Equals(18));
            Console.WriteLine(b + 10);
        }
    }
}
