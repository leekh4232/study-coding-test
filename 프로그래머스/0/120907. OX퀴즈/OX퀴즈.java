import java.util.Arrays;

public class Solution {

    public static String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];

        for (int i = 0; i < quiz.length; i++) {
            String[] expr = quiz[i].split(" ");
            int num1 = Integer.parseInt(expr[0]);
            int num2 = Integer.parseInt(expr[2]);
            int num3 = Integer.parseInt(expr[4]);

            boolean result;
            if (expr[1].equals("+")) {
                result = (num1 + num2 == num3);
            } else {
                result = (num1 - num2 == num3);
            }

            answer[i] = result ? "O" : "X";
        }

        return answer;
    }

    public static void main(String[] args) {
        String[] test1 = {"3 - 4 = -3", "5 + 6 = 11"};
        String[] test2 = {"19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"};

        // 기본 API를 이용한 출력
        System.out.println(Arrays.toString(solution(test1))); // [X, O]
        System.out.println(Arrays.toString(solution(test2))); // [O, O, X, O]
    }
}
