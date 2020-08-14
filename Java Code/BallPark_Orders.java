import java.util.Scanner;

public class BallPark_Orders {
	static final double TAX=1.07;
	static double price(String[] foods_name) {
		double total=0;
		double unit_price=0;
		for (String food : foods_name) {
			switch(food.toLowerCase()) {
				case "pizza":
				case "nachos":
					unit_price=6.0;
					break;
				case "cheeseburger":
					unit_price=10.0;
					break;
				case "water":
					unit_price=4.0;
					break;
				default:
					unit_price=5.0;
					break;
				}
			total += unit_price;
		}
		System.out.println(total);
		return TAX*total;
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String names=sc.nextLine();
		String[] foods=names.split(" ");
		sc.close();
		System.out.printf("%1.2f",price(foods));
	}

}
