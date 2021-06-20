/**
 * The member states of the UN are planning to send  people to the moon. They want them to be from different countries. You will be given a list of pairs of astronaut ID's. Each pair is made of astronauts from the same country. Determine how many pairs of astronauts from different countries they can choose from.
 * <p>
 * Example
 * <p>
 * <p>
 * <p>
 * There are  astronauts numbered  through . Astronauts grouped by country are  and . There are  pairs to choose from:  and .
 * <p>
 * Function Description
 * <p>
 * Complete the journeyToMoon function in the editor below.
 * <p>
 * journeyToMoon has the following parameter(s):
 * <p>
 * int n: the number of astronauts
 * int astronaut[p][2]: each element  is a  element array that represents the ID's of two astronauts from the same country
 * Returns
 * - int: the number of valid pairs
 * <p>
 * Input Format
 * <p>
 * The first line contains two integers  and , the number of astronauts and the number of pairs.
 * Each of the next  lines contains  space-separated integers denoting astronaut ID's of two who share the same nationality.
 * <p>
 * Constraints
 * <p>
 * Sample Input 0
 * <p>
 * 5 3
 * 0 1
 * 2 3
 * 0 4
 * Sample Output 0
 * <p>
 * 6
 * Explanation 0
 * <p>
 * Persons numbered  belong to one country, and those numbered  belong to another. The UN has  ways of choosing a pair:
 * <p>
 * <p>
 * Sample Input 1
 * <p>
 * 4 1
 * 0 2
 * Sample Output 1
 * <p>
 * 5
 * Explanation 1
 * <p>
 * Persons numbered  belong to the same country, but persons  and  don't share countries with anyone else. The UN has  ways of choosing a pair:
 */

import java.io.*;
import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

public class JourneyToTheMoon {

    static class Result {

        /*
         * Complete the 'journeyToMoon' function below.
         *
         * The function is expected to return an INTEGER.
         * The function accepts following parameters:
         *  1. INTEGER n
         *  2. 2D_INTEGER_ARRAY astronaut
         */

        public static long journeyToMoon(int n, List<List<Integer>> astronaut) {
            // Write your code here
            Map<Integer, Set<Integer>> countryMapping = new HashMap<>();
            for (List<Integer> pair : astronaut) {
                int first = pair.get(0), second = pair.get(1);

                boolean firstFound = countryMapping.containsKey(first), secondFound = countryMapping.containsKey(second);
                if (!firstFound && !secondFound) {
                    Set<Integer> astronauts = new HashSet<>(Arrays.asList(first, second));
                    countryMapping.put(first, astronauts);
                    countryMapping.put(second, astronauts);
                } else if (!firstFound && secondFound) {
                    Set<Integer> astronauts = countryMapping.get(second);
                    astronauts.add(first);
                    countryMapping.put(first, astronauts);
                } else if (firstFound && !secondFound) {
                    Set<Integer> astronauts = countryMapping.get(first);
                    astronauts.add(second);
                    countryMapping.put(second, astronauts);
                } else {
                    Set<Integer> astronautsFirst = countryMapping.get(first);
                    Set<Integer> astronautsSecond = countryMapping.get(second);
                    astronautsFirst.addAll(astronautsSecond);
                    for (Integer single : astronautsSecond) {
                        countryMapping.put(single, astronautsFirst);
                    }
                }
            }
            long result = 0;
            for (int i = 0; i < n; i++) {
                if (!countryMapping.containsKey(i))
                    countryMapping.put(i, new HashSet<>(Collections.singletonList(i)));
            }
            for (Set<Integer> countryAstronauts : countryMapping.values().stream().distinct().collect(toList())) {
                result += countryAstronauts.size() * (n - countryAstronauts.size());
            }
            return result / 2;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int p = Integer.parseInt(firstMultipleInput[1]);

        List<List<Integer>> astronaut = new ArrayList<>();

        IntStream.range(0, p).forEach(i -> {
            try {
                astronaut.add(
                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                .map(Integer::parseInt)
                                .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        long result = Result.journeyToMoon(n, astronaut);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
