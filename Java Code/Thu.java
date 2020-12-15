class MyThread extends Thread {
    public void run() {
        System.out.println("Dung roi");
    }
}
public class Thu {
    public static void main(String[] args){
        MyThread mt =new MyThread();
        mt.start();
    }

}