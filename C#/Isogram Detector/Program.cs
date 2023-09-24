/*
	An isogram is a word that has no repeating letters, whether they are consecutive or non-consecutive.  
	Your job is to find a way to detect if a word is an isogram.

	Task: Write a program that takes in a string as input, detects if the string is an isogram and outputs true or false based on the result.
 
	Input Format: 
		A string containing one word.

	Output Format: 
		A string: true or false.

	Sample Input: 
		turbulence

	Sample Output: 
		false

Created by Ueda
*/

namespace Isogram_Detector;
class Program
{
    static string  isDoubled (string? st){
        if (!string.IsNullOrEmpty(st)) {
            string?  temp = new string(""); 
            foreach(var c in st){
                if(temp.IndexOf(c) == -1){
                    temp += c;
                } else return "false";
            }
        }
        return "true";
    }
    static void Main(string[] args)
    {
        string? word = Console.ReadLine();
        Console.WriteLine(isDoubled(word));
    }
}
