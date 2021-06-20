/**
 * An English text needs to be encrypted using the following encryption scheme. First, the spaces are removed from the
 * text. Let  be the length of this text. Then, characters are written into a grid, whose rows and columns have the
 * following constraints:
 * <p>
 * Example
 * After removing spaces, the string is  characters long.  is between  and , so it is written in the form of a grid with
 * 7 rows and 8 columns.
 * <p>
 * ifmanwas
 * meanttos
 * tayonthe
 * groundgo
 * dwouldha
 * vegivenu
 * sroots
 * <p>
 * Ensure that
 * If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. The encoded message is
 * obtained by displaying the characters of each column, with a space between column texts. The encoded message for the
 * grid above is:
 * <p>
 * imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau
 * <p>
 * Create a function to encode a message.
 * <p>
 * Function Description
 * <p>
 * Complete the encryption function in the editor below.
 * <p>
 * encryption has the following parameter(s):
 * <p>
 * string s: a string to encrypt
 * Returns
 * <p>
 * string: the encrypted string
 * Input Format
 * <p>
 * One line of text, the string
 * <p>
 * Constraints
 * contains characters in the range ascii[a-z] and space, ascii(32).
 * <p>
 * Sample Input
 * <p>
 * haveaniceday
 * Sample Output 0
 * <p>
 * hae and via ecy
 * Explanation 0
 * <p>
 * ,  is between  and .
 * Rewritten with  rows and  columns:
 * <p>
 * have
 * anic
 * eday
 * Sample Input 1
 * <p>
 * feedthedog
 * Sample Output 1
 * <p>
 * fto ehg ee dd
 * Explanation 1
 * <p>
 * ,  is between  and .
 * Rewritten with  rows and  columns:
 * <p>
 * feed
 * thed
 * og
 * Sample Input 2
 * <p>
 * chillout
 * Sample Output 2
 * <p>
 * clu hlt io
 * Explanation 2
 * <p>
 * ,  is between  and .
 * Rewritten with  columns and  rows ( so we have to use .)
 * <p>
 * chi
 * llo
 * ut
 */

import java.io.*;

public class Encryption {
    static class Result {
        /*
         * Complete the 'encryption' function below.
         *
         * The function is expected to return a STRING.
         * The function accepts STRING s as parameter.
         */

        public static String encryption(String s) {
            String spaceFilteredText = s.replace(" ", "");
            int[] dimensions = Result.findProperRowAndColumn(spaceFilteredText);
            int row = dimensions[0], column = dimensions[1];
            char[][] tableau = new char[row][column];

            for (int i = 0; i < spaceFilteredText.length(); i++) {
                tableau[i / column][i % column] = spaceFilteredText.charAt(i);
            }

            StringBuilder result = new StringBuilder();
            for (int i = 0; i < column; i++) {
                for (int j = 0; j < row; j++) {
                    char ch = tableau[j][i];
                    if (ch != 0) {
                        result.append(ch);
                    } else {
                        break;
                    }
                }
                result.append(" ");
            }
            return result.toString();
        }

        private static int[] findProperRowAndColumn(String s) {
            double squareRootOfLength = Math.sqrt(s.length());
            int min = (int) Math.floor(squareRootOfLength), max = (int) Math.ceil(squareRootOfLength);
            if (min == max) {
                return new int[]{min, max};
            }
            if (min * max >= s.length())
                return new int[]{min, max};
            else
                return new int[]{max, max};
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        String s = bufferedReader.readLine();

        String result = Result.encryption(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}