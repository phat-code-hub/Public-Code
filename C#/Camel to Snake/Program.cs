namespace Camel_to_Snake;
using System.Text;
class Program
{
    static void Main(string[] args)
    {
        String st0 = Console.ReadLine();
        StringBuilder sb = new StringBuilder();
        for (int i=0;i<st0.Length;i++){
            if(char.IsUpper(st0[i])) {
                if (i>0) sb.Append('_');
                sb.Append(char.ToLower(st0[i]));
            } 
            else sb.Append(st0[i]);
        }
        Console.WriteLine(sb);
    }
}
