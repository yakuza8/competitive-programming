/**
 * David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.
 * <p>
 * David wants to perform some number of swap operations such that:
 * <p>
 * Each container contains only balls of the same type.
 * No two balls of the same type are located in different containers.
 * Example
 * <p>
 * <p>
 * David has  containers and  different types of balls, both of which are numbered from  to . The distribution of ball types per container are shown in the following diagram.
 * <p>
 * image
 * <p>
 * In a single operation, David can swap two balls located in different containers.
 * <p>
 * The diagram below depicts a single swap operation:
 * <p>
 * image
 * <p>
 * In this case, there is no way to have all green balls in one container and all red in the other using only swap operations. Return Impossible.
 * <p>
 * You must perform  queries where each query is in the form of a matrix, . For each query, print Possible on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print Impossible.
 * <p>
 * Function Description
 * <p>
 * Complete the organizingContainers function in the editor below.
 * <p>
 * organizingContainers has the following parameter(s):
 * <p>
 * int containter[n][m]: a two dimensional array of integers that represent the number of balls of each color in each container
 * Returns
 * <p>
 * string: either Possible or Impossible
 * Input Format
 * <p>
 * The first line contains an integer , the number of queries.
 * <p>
 * Each of the next  sets of lines is as follows:
 * <p>
 * The first line contains an integer , the number of containers (rows) and ball types (columns).
 * Each of the next  lines contains  space-separated integers describing row .
 * Constraints
 * <p>
 * Scoring
 * <p>
 * For  of score, .
 * For  of score, .
 * Output Format
 * <p>
 * For each query, print Possible on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print Impossible.
 * <p>
 * Sample Input 0
 * <p>
 * 2
 * 2
 * 1 1
 * 1 1
 * 2
 * 0 2
 * 1 1
 * Sample Output 0
 * <p>
 * Possible
 * Impossible
 * Explanation 0
 * <p>
 * We perform the following  queries:
 * <p>
 * The diagram below depicts one possible way to satisfy David's requirements for the first query: image
 * Thus, we print Possible on a new line.
 * The diagram below depicts the matrix for the second query: image
 * No matter how many times we swap balls of type  and  between the two containers, we'll never end up with one container only containing type  and the other container only containing type . Thus, we print Impossible on a new line.
 * Sample Input 1
 * <p>
 * 2
 * 3
 * 1 3 1
 * 2 1 2
 * 3 3 3
 * 3
 * 0 2 1
 * 1 1 1
 * 2 0 0
 * Sample Output 1
 * <p>
 * Impossible
 * Possible
 */

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

public class OrganizingBallsOfContainers {
    static class Result {

        /*
         * Complete the 'organizingContainers' function below.
         *
         * The function is expected to return a STRING.
         * The function accepts 2D_INTEGER_ARRAY container as parameter.
         */

        public static String organizingContainers(List<List<Integer>> container) {
            // Write your code here
            for (int i = 0; i < container.size() - 1; i++) {
                long sumOfCurrentColumn = Result.sumOfCurrentColumnExpectItself(i, container);
                long sumOfOtherCurrentRow = Result.sumOfCurrentRowExpectItself(i, container);
                if (sumOfCurrentColumn != sumOfOtherCurrentRow) {
                    return "Impossible";
                } else {
                    int m = i;
                    List<Integer> currentRow = container.get(i);
                    List<Integer> currentColumn = container.stream().map(row -> row.get(m)).collect(toList());

                    for (int j = i + 1; j < currentColumn.size(); j++) {
                        int replaceValue = currentColumn.get(j);
                        int k = i + 1;
                        while (replaceValue != 0) {
                            int rowValue = currentRow.get(k);
                            int minValue = rowValue < replaceValue ? rowValue : replaceValue;
                            currentRow.set(k, rowValue - minValue);
                            container.get(j).set(k, container.get(j).get(k) + minValue);
                            replaceValue -= minValue;

                            if (replaceValue != 0) {
                                k++;
                            } else {
                                container.get(j).set(i, 0);
                                break;
                            }
                        }
                    }
                }

            }
            return "Possible";
        }

        private static long sumOfCurrentColumnExpectItself(int i, List<List<Integer>> container) {
            long sum = 0;
            for (int j = 0; j < container.size(); j++) {
                sum += container.get(j).get(i);
            }
            return sum - container.get(i).get(i);
        }

        private static long sumOfCurrentRowExpectItself(int i, List<List<Integer>> container) {
            long sum = 0;
            for (int j = 0; j < container.size(); j++) {
                sum += container.get(i).get(j);
            }
            return sum - container.get(i).get(i);
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, q).forEach(qItr -> {
            try {
                int n = Integer.parseInt(bufferedReader.readLine().trim());

                List<List<Integer>> container = new ArrayList<>();

                IntStream.range(0, n).forEach(i -> {
                    try {
                        container.add(
                                Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                        .map(Integer::parseInt)
                                        .collect(toList())
                        );
                    } catch (IOException ex) {
                        throw new RuntimeException(ex);
                    }
                });

                String result = Result.organizingContainers(container);

                bufferedWriter.write(result);
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

/*
1
4
0 0 5 0
4 0 0 0
0 2 0 1
0 1 0 2
 */