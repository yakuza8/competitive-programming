/**
 * Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.
 *
 * Example
 *
 *
 * There are three values that differ by : , , and . Return .
 *
 * Function Description
 *
 * Complete the pairs function below.
 *
 * pairs has the following parameter(s):
 *
 * int k: an integer, the target difference
 * int arr[n]: an array of integers
 * Returns
 *
 * int: the number of pairs that satisfy the criterion
 * Input Format
 *
 * The first line contains two space-separated integers  and , the size of  and the target value.
 * The second line contains  space-separated integers of the array .
 *
 * Constraints
 *
 * each integer  will be unique
 * Sample Input
 *
 * STDIN       Function
 * -----       --------
 * 5 2         arr[] size n = 5, k =2
 * 1 5 3 4 2   arr = [1, 5, 3, 4, 2]
 * Sample Output
 *
 * 3
 * Explanation
 *
 * There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1]. .
 */

import java.io.*;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

public class Pairs {

    static class Result {

        /*
         * Complete the 'pairs' function below.
         *
         * The function is expected to return an INTEGER.
         * The function accepts following parameters:
         *  1. INTEGER k
         *  2. INTEGER_ARRAY arr
         */

        public static int pairs(int k, List<Integer> arr) {
            // Write your code here
            int result = 0;
            Set<Integer> values = new HashSet<>();
            for (Integer number: arr) {
                values.add(number);
            }
            for (Integer number: values) {
                result += values.contains(number - k) ? 1 : 0;
                result += values.contains(number + k) ? 1 : 0;
            }
            return result / 2;
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int k = Integer.parseInt(firstMultipleInput[1]);

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int result = Result.pairs(k, arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
