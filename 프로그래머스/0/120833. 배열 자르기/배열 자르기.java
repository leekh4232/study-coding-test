import java.util.Arrays;

public class Solution {
    public static int[] solution(int[] numbers, int num1, int num2) {
        return Arrays.copyOfRange(numbers, num1, num2 + 1);
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{1, 2, 3, 4, 5}, 1, 3))); // [2, 3, 4]
        System.out.println(Arrays.toString(solution(new int[]{1, 3, 5}, 1, 2)));       // [3, 5]
    }
}