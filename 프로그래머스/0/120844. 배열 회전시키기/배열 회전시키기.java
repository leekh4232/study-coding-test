import java.util.Arrays;

public class Solution {

    public static int[] solution(int[] numbers, String direction) {
        int len = numbers.length;
        int[] answer = new int[len];

        if ("right".equals(direction)) {
            answer[0] = numbers[len - 1];  // 마지막 원소를 맨 앞으로
            for (int i = 0; i < len - 1; i++) {
                answer[i + 1] = numbers[i];
            }
        } else if ("left".equals(direction)) {
            for (int i = 1; i < len; i++) {
                answer[i - 1] = numbers[i];
            }
            answer[len - 1] = numbers[0];  // 첫 번째 원소를 맨 뒤로
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{1, 2, 3}, "right"))); 
        // [3, 1, 2]
        System.out.println(Arrays.toString(solution(new int[]{4, 455, 6, 4, -1, 45, 6}, "left"))); 
        // [455, 6, 4, -1, 45, 6, 4]
    }
}
