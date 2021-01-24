using System;

namespace Text_Decompressor
{
    class Program
    {
        static string decompressed_Text="";
        static string num_str = "";
        //-------------------------------------------------------------------------------
        //Decomresss  letter method
        static string repeat_Char(char letter,int repeatTimes)
        {
            string temp = "";
            if (repeatTimes >0) for (int i = 1; i <= repeatTimes; i++) temp += letter;
            return temp;
        }
        //-------------------------------------------------------------------------------
        //Decompress char
        static void replace_LastChar()
        {
            char replaceLetter = char.Parse(decompressed_Text.Substring(decompressed_Text.Length - 1));
            string repeatText = repeat_Char(replaceLetter, Convert.ToInt32(num_str));
            decompressed_Text = decompressed_Text.Remove(decompressed_Text.Length - 1);
            decompressed_Text += repeatText;
        }
        //-------------------------------------------------------------------------------
        //Main Code
        static void Main(string[] args)
        {
            String compressed_Text = Console.ReadLine();
            if (compressed_Text.Length>0)
            {
                int i = 0;
                char[] chs = compressed_Text.ToCharArray();
                //analyse until last character
                do
                {
                    //char is a number
                    if (char.IsNumber(chs[i])) num_str += chs[i];
                    // char is not a number
                    else
                    {
                        if (num_str.Length>0)
                        {
                            replace_LastChar();
                            num_str = "";
                        }
                        decompressed_Text += chs[i].ToString();
                    }
                    i++;
                } while (i < chs.Length);
                //Replace last letter if last append char is a number
                if (num_str.Length > 0) replace_LastChar();
                Console.WriteLine(decompressed_Text);
            }
            
        }
    }
}
