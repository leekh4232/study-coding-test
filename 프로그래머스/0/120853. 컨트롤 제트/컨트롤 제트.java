public class Solution {

    public static int solution(String s) {
        String[] tokens = s.split(" ");
        int sum = 0;
        int last = 0;

        for (String token : tokens) {
            if (token.equals("Z")) {
                sum -= last; // 직전 값 무효화
            } else {
                last = Integer.parseInt(token);
                sum += last;
            }
        }

        return sum;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution("1 2 Z 3"));          // 4
        System.out.println(solution("10 20 30 40"));      // 100
        System.out.println(solution("10 Z 20 Z 1"));      // 1
        System.out.println(solution("10 Z 20 Z"));        // 0
        System.out.println(solution("-1 -2 -3 Z"));       // -3
    }
}
