package Challenge;

import java.util.HashMap;
import java.util.Scanner;
import java.util.Map.Entry;

class Bowling {
    HashMap<String, Integer> players;

    public Bowling() {
        players = new HashMap<String, Integer>();
    }

    public void addPlayer(String name, int p) {
        players.put(name, p);
    }

    public void getWinner() {
        int max = 0;
        String player="";
        for (Entry<String, Integer> winner : players.entrySet()) {
            if (winner.getValue() >max) {
                max=winner.getValue();
                player=winner.getKey();
            }
        }
        System.out.println(player);
    }
}
public class BowlingGame {
    public static void main(String[] args) {
        Bowling game = new Bowling();
        Scanner sc=new Scanner(System.in);
        for (int i=0;i<3;i++){
            String input =sc.nextLine();
            String[] values = input.split(" ");
            String name= values[0];
            int points=Integer.parseInt(values[1]);
            game.addPlayer(name, points);
        }
        game.getWinner();
        sc.close();
    }
}
