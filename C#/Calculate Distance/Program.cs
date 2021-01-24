using System;
using System.Data;
using System.Globalization;
using System.Runtime.InteropServices;

namespace Calculate_Distance
{
  
    class Program
        
    {
        //Prepare class contains point coordinate
        class Point
        {
            private double x;
            private double y;
            public Point(double x, double y)
            {
                this.x = x;
                this.y = y;
            }
            public double X
            {
                get { return this.x; }
            }
            public double Y
            {
                get { return this.y; }
            }
            public override string ToString()
            {
                return string.Format("X ={0}, Y={1}",this.X,this.Y);
            }
        }
        //-----------------------------------------------------------
        // Initial and assign to new Point
        static Point init(string cord)
        {
            //Remove "("and ")" letter
            string txt = cord.Remove(0,1);
            txt=txt.Remove(txt.Length - 1,1);
            string[] nums_ = txt.Split(",");
            //Convert to double
            double cordX =Convert.ToDouble(nums_[0]);
            double cordY = Convert.ToDouble(nums_[1]);
            return new Point(cordX, cordY);
        }
        //-----------------------------------------------------------
        //Calculate and output result
        static void distance(Point p1,Point p2)
        {
            double result = Math.Sqrt(Math.Pow((p2.X-p1.X),2)+Math.Pow((p2.Y-p1.Y),2));
            Console.WriteLine(Math.Round(result,2));
        }
        //-----------------------------------------------------------
        //Main Code
        static void Main(string[] args)
        {
            Console.WriteLine("Input 2 points coordinates (x1,y1) (x2,y2):");
            string[] cords = Console.ReadLine().Trim().Split();
            if(cords.Length==2)
            {
                //Assign input data to 2 points 
                Point p1 = init(cords[0]);
                Point p2 = init(cords[1]);
                // Commnent out below 3 codes to show 2 calculated points' data
                //Console.WriteLine("Two input points :");
                //Console.WriteLine(p1);
                //Console.WriteLine(p2);
                distance(p1, p2);
            }
            
        }
    }
}
