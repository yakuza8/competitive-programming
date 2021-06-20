/**
 * Use the counting sort to order a list of strings associated with integers. If two strings are associated with the same integer, they must be printed in their original order, i.e. your sorting algorithm should be stable. There is one other twist: strings in the first half of the array are to be replaced with the character - (dash, ascii 45 decimal).
 *
 * Insertion Sort and the simple version of Quicksort are stable, but the faster in-place version of Quicksort is not since it scrambles around elements while sorting.
 *
 * Design your counting sort to be stable.
 *
 * Example
 *
 * The first two strings are replaced with '-'. Since the maximum associated integer is , set up a helper array with at least two empty arrays as elements. The following shows the insertions into an array of three empty arrays.
 *
 * i	string	converted	list
 * 0				[[],[],[]]
 * 1 	a 	-		[[-],[],[]]
 * 2	b	-		[[-],[-],[]]
 * 3	c			[[-,c],[-],[]]
 * 4	d			[[-,c],[-,d],[]]
 * The result is then printed:  .
 *
 * Function Description
 *
 * Complete the countSort function in the editor below. It should construct and print the sorted strings.
 *
 * countSort has the following parameter(s):
 *
 * string arr[n][2]: each arr[i] is comprised of two strings, x and s
 * Returns
 * - Print the finished array with each element separated by a single space.
 *
 * Note: The first element of each , , must be cast as an integer to perform the sort.
 *
 * Input Format
 *
 * The first line contains , the number of integer/string pairs in the array .
 * Each of the next  contains  and , the integers (as strings) with their associated strings.
 *
 * Constraints
 *
 *
 *  is even
 *
 *
 *  consists of characters in the range
 *
 * Output Format
 *
 * Print the strings in their correct order, space-separated on one line.
 *
 * Sample Input
 *
 * 20
 * 0 ab
 * 6 cd
 * 0 ef
 * 6 gh
 * 4 ij
 * 0 ab
 * 6 cd
 * 0 ef
 * 6 gh
 * 0 ij
 * 4 that
 * 3 be
 * 0 to
 * 1 be
 * 5 question
 * 1 or
 * 2 not
 * 4 is
 * 2 to
 * 4 the
 * Sample Output
 *
 * - - - - - to be or not to be - that is the question - - - -
 * Explanation
 *
 * The correct order is shown below. In the array at the bottom, strings from the first half of the original array were replaced with dashes.
 *
 * 0 ab
 * 0 ef
 * 0 ab
 * 0 ef
 * 0 ij
 * 0 to
 * 1 be
 * 1 or
 * 2 not
 * 2 to
 * 3 be
 * 4 ij
 * 4 that
 * 4 is
 * 4 the
 * 5 question
 * 6 cd
 * 6 gh
 * 6 cd
 * 6 gh
 * sorted = [['-', '-', '-', '-', '-', 'to'], ['be', 'or'], ['not', 'to'], ['be'], ['-', 'that', 'is', 'the'], ['question'], ['-', '-', '-', '-'], [], [], [], []]
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

public class TheFullCountingSort {

    static class Result {

        /*
         * Complete the 'countSort' function below.
         *
         * The function accepts 2D_STRING_ARRAY arr as parameter.
         */

        public static void countSort(List<List<String>> arr) {
            // Write your code here
            HashMap<String, List<String>> orderedMap = new HashMap<>();
            Set<Integer> keySey = new TreeSet<>();
            int length = arr.size(), halfLength = length / 2;
            for (int i = 0; i < length; i++) {
                String number = arr.get(i).get(0), text = arr.get(i).get(1);
                keySey.add(Integer.parseInt(number));

                if (!orderedMap.containsKey(number)) {
                    orderedMap.put(number, new ArrayList<>());
                }

                if (i < halfLength) {
                    orderedMap.get(number).add("-");
                } else {
                    orderedMap.get(number).add(text);
                }
            }
            StringBuilder result = new StringBuilder();
            for (Integer key: keySey) {
                for (String s: orderedMap.get(key.toString())) {
                    result.append(s);
                    result.append(" ");
                }
            }
            System.out.println(result.substring(0, result.length() - 1));
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<String>> arr = new ArrayList<>();

        IntStream.range(0, n).forEach(i -> {
            try {
                arr.add(
                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        Result.countSort(arr);

        bufferedReader.close();
    }
}
