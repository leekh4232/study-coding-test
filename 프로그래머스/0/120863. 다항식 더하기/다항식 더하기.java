public class Solution {
    public static String solution(String polynomial) {
        // [x 계수 합, 상수항 합]
        int xSum = 0;
        int constSum = 0;

        // 다항식을 " + " 기준으로 나눔
        String[] poly = polynomial.split(" \\+ ");

        for (String p : poly) {
            if (p.equals("x")) {
                xSum += 1;
            } else if (p.endsWith("x")) {
                xSum += Integer.parseInt(p.substring(0, p.length() - 1));
            } else {
                constSum += Integer.parseInt(p);
            }
        }

        // 결과 조합
        StringBuilder answer = new StringBuilder();

        if (xSum > 1) {
            answer.append(xSum).append("x");
        } else if (xSum == 1) {
            answer.append("x");
        }

        if (constSum > 0) {
            if (answer.length() > 0) {
                answer.append(" + ");
            }
            answer.append(constSum);
        }

        return answer.toString();
    }

    // ✅ 예제 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution("3x + 7 + x"));       // "4x + 7"
        System.out.println(solution("x + x + x"));        // "3x"
        System.out.println(solution("5 + 3 + 7"));        // "15"
        System.out.println(solution("2x + 5 + x + 3"));   // "3x + 8"
    }
}
