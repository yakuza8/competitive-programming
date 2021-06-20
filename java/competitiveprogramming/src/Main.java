import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        List<Integer> grades = Arrays.asList(75, 67, 40, 33);

        List<Integer> result = grades.stream().map(grade -> {
            if (grade <= 38)
                return grade;
            else {
                int amountToNext5 = grade % 5;
                return amountToNext5 < 3 ? grade + amountToNext5 : grade;
            }
        }).collect(Collectors.toList());
    }
}
