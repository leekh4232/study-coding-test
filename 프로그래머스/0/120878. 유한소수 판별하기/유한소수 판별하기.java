public class Solution {

    public static int solution(int a, int b) {
        int answer = 2;

        // 최대공약수(GCD)를 구함
        int gcd = getGCD(a, b);

        // 기약분수의 분모를 계산
        b /= gcd;

        // 분모에서 2 제거
        while (b % 2 == 0) {
            b /= 2;
        }

        // 분모에서 5 제거
        while (b % 5 == 0) {
            b /= 5;
        }

        // 남은 값이 1이면 유한소수
        if (b == 1) {
            answer = 1;
        }

        return answer;
    }

    // 유클리드 호제법으로 GCD 계산
    private static int getGCD(int x, int y) {
        while (y != 0) {
            int temp = x % y;
            x = y;
            y = temp;
        }
        return x;
    }

    // ✅ 테스트용 main
    public static void main(String[] args) {
        System.out.println(solution(7, 20));   // 출력: 1
        System.out.println(solution(11, 22));  // 출력: 1
        System.out.println(solution(12, 21));  // 출력: 2
    }
}
