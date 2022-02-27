using System;
using System.Linq;

namespace CreditCard_Validator_Luhn_Method
{
    class Program
    {
        //Run LuhnTest
        static bool checkCard(string card)
        {
            int[] num = new int[card.Length];
            char[] digits = card.ToCharArray();
            //Reverse digits
            Array.Reverse(digits);
            int temp;
            for(var i = 0; i < digits.Length; i++)
            {
                //temp = (int)char.GetNumericValue(digits[i]);
                temp = Convert.ToInt32(digits[i] - '0');
                if ((i % 2) != 0)
                {
                    //Multiply digits at even position twice
                    temp *= 2;
                    //subtract 9 of digits larger than 9
                    temp = temp <= 9 ? temp : temp - 9;
                }
                num[i] = temp;
            }
            foreach (int n in num) Console.Write(n + ",");
            Console.WriteLine();
            Console.WriteLine(num.Sum());
            //card is valid if sum of digits modulus 10 equal 0
            return ((num.Sum()) % 10 == 0) ? true : false;
        }
        static void Main(string[] args)
        {
            bool isValid = false;
            String cardId = Console.ReadLine();
            //checkCard length 
            if (cardId.Length == 16) isValid=checkCard(cardId.Trim());
            Console.WriteLine(isValid?"valid":"not valid");
        }
    }
}
