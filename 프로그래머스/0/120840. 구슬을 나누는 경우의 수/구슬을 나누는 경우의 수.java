import java.math.BigInteger;

public class Solution {
    // BigInteger로 팩토리얼을 계산하는 메서드
    public BigInteger facto(int n) {
        BigInteger f = BigInteger.ONE; // 초기값 1 설정

        for (int i = 1; i <= n; i++) { // 1부터 n까지 곱셈
            f = f.multiply(BigInteger.valueOf(i));
        }

        return f; // 계산된 팩토리얼 반환
    }

    public int solution(int balls, int share) {
        if (balls == share || share == 0) {
            return 1;
        }

        // 조합 공식: C(n, r) = n! / ((n - r)! * r!)
        BigInteger numerator = facto(balls);
        BigInteger denominator = facto(balls - share).multiply(facto(share));
        BigInteger result = numerator.divide(denominator); // 조합 값 계산

        return result.intValue(); // 최종 결과 반환
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 테스트 예제 실행
        System.out.println(s.solution(3, 2));  // 3
        System.out.println(s.solution(5, 3));  // 10
        System.out.println(s.solution(30, 15)); // 큰 값도 정상적으로 처리 가능
    }
}
