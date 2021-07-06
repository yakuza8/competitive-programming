/**
 * An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:
 * <p>
 * The player with the highest score is ranked number  on the leaderboard.
 * Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
 * Example
 * <p>
 * <p>
 * <p>
 * The ranked players will have ranks , , , and , respectively. If the player's scores are ,  and , their rankings after each game are ,  and . Return .
 * <p>
 * Function Description
 * <p>
 * Complete the climbingLeaderboard function in the editor below.
 * <p>
 * climbingLeaderboard has the following parameter(s):
 * <p>
 * int ranked[n]: the leaderboard scores
 * int player[m]: the player's scores
 * Returns
 * <p>
 * int[m]: the player's rank after each new score
 * Input Format
 * <p>
 * The first line contains an integer , the number of players on the leaderboard.
 * The next line contains  space-separated integers , the leaderboard scores in decreasing order.
 * The next line contains an integer, , the number games the player plays.
 * The last line contains  space-separated integers , the game scores.
 * <p>
 * Constraints
 * <p>
 * for
 * for
 * The existing leaderboard, , is in descending order.
 * The player's scores, , are in ascending order.
 * Subtask
 * <p>
 * For  of the maximum score:
 * <p>
 * Sample Input 1
 * <p>
 * CopyDownload
 * Array: ranked
 * 100
 * 100
 * 50
 * 40
 * 40
 * 20
 * 10
 * <p>
 * <p>
 * <p>
 * <p>
 * <p>
 * Array: player
 * 5
 * 25
 * 50
 * 120
 * <p>
 * <p>
 * 7
 * 100 100 50 40 40 20 10
 * 4
 * 5 25 50 120
 * Sample Output 1
 * <p>
 * 6
 * 4
 * 2
 * 1
 * Explanation 1
 * <p>
 * Alice starts playing with  players already on the leaderboard, which looks like this:
 * <p>
 * image
 * <p>
 * After Alice finishes game , her score is  and her ranking is :
 * <p>
 * image
 * <p>
 * After Alice finishes game , her score is  and her ranking is :
 * <p>
 * image
 * <p>
 * After Alice finishes game , her score is  and her ranking is tied with Caroline at :
 * <p>
 * image
 * <p>
 * After Alice finishes game , her score is  and her ranking is :
 * <p>
 * image
 * <p>
 * <p>
 * Sample Input 2
 * <p>
 * CopyDownload
 * Array: ranked
 * 100
 * 90
 * 90
 * 80
 * 75
 * 60
 * <p>
 * <p>
 * <p>
 * <p>
 * <p>
 * Array: player
 * 50
 * 65
 * 77
 * 90
 * 102
 * <p>
 * <p>
 * 6
 * 100 90 90 80 75 60
 * 5
 * 50 65 77 90 102
 * Sample Output 2
 * <p>
 * 6
 * 5
 * 4
 * 2
 * 1
 */

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class ClimbingTheLeaderboard {
    static class Result {

        /*
         * Complete the 'climbingLeaderboard' function below.
         *
         * The function is expected to return an INTEGER_ARRAY.
         * The function accepts following parameters:
         *  1. INTEGER_ARRAY ranked
         *  2. INTEGER_ARRAY player
         */

        public static List<Integer> climbingLeaderboard(List<Integer> ranked, List<Integer> player) {
            // Write your code here
            List<Integer> result = new ArrayList<>();

            int position = 0, rank = 1, lastSeenScore = -1;

            while (player.size() != 0) {
                int lastIndex = player.size() - 1;
                int currentScore = player.get(lastIndex), currentSeenScore = position < ranked.size() ? ranked.get(position) : -1;

                while (currentScore < currentSeenScore) {
                    if (lastSeenScore != currentSeenScore)
                        rank++;
                    lastSeenScore = currentSeenScore;
                    position++;
                    if (position >= ranked.size())
                        break;
                    currentSeenScore = ranked.get(position);
                }
                result.add(0, rank);

                player.remove(lastIndex);
            }

            return result;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int rankedCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> ranked = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int playerCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> player = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        List<Integer> result = Result.climbingLeaderboard(ranked, player);

        bufferedWriter.write(
                result.stream()
                        .map(Object::toString)
                        .collect(joining("\n"))
                        + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}
