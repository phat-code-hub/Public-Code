package Challenge;

import java.util.Scanner;
abstract class Shape {
    int width;
    abstract void area();
}
class Square extends Shape {
    public Square(int width){
        this.width=width;
    }
    @Override
    void area() {
      System.out.println(this.width*this.width);   
    }
}
class Circle extends Shape {
    public Circle(int diameter){
        this.width=diameter;
    }
    @Override
    void area() {
        System.out.println(Math.PI*this.width*this.width);
    }  
}
public class Shapes {
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        int x =sc.nextInt();
        int y=sc.nextInt();
        Square a=new Square(x);
        Circle b=new Circle(y);
        a.area();
        b.area();
        sc.close();
    }
}
