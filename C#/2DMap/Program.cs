namespace _2DMap;
using System.Text;
using System;
class Program
{
    // static int distance(string cords_str) {
    //     string[] cords  = cords_str.Split(',');
    //     int X1=0,X2=0;
    //     int Y1=0,Y2=0;
    //     int count=0;
    //     for(int i=0;i<cords.Count();i++ ){
    //         for (int j=0; j<cords[i].Count();j++){
    //             if (cords[i][j] == 'P'){
    //                 if (count == 0) {
    //                     X1=i;
    //                     Y1=j;
    //                     count++;
    //                 } else {
    //                     X2=i;
    //                     Y2=j;
    //                     break;
    //                 }
    //             }
    //         }
    //         if (count==2) break;
    //     }
    //     return Math.Abs(X1-X2)+Math.Abs(Y1-Y2);
    // }
    static void Main(string[] args)
    {
        Console.WriteLine("Nhap toa do: ");
        string map0=Console.ReadLine();
        // Console.WriteLine(distance(map));
        StringBuilder map = new StringBuilder("");
        foreach(char c in map0){
            if (c is not ',') map.Append(c);
        }
        // Console.WriteLine(map);
        int[] idx = new int[2];
        map0 = map.ToString();
        int count=0;
        for(int i=0;i<map0.Length;i++){
            if (map0[i]== 'P') idx[count++] =i;
        };
        int res = Math.Abs(idx[0]/5- idx[1]/5)+ Math.Abs(idx[0]%5- idx[1]%5);
        Console.WriteLine(res);
    }
}
