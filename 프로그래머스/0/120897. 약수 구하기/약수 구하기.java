import java.util.*;

public class Solution {

    public static int[] solution(int n) {
        List<Integer> divisors = new ArrayList<>();

        // 1부터 n까지 반복하며 약수 확인
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                divisors.add(i);
            }
        }

        // List<Integer> → int[] 변환
        int[] answer = new int[divisors.size()];
        for (int i = 0; i < divisors.size(); i++) {
            answer[i] = divisors.get(i);
        }

        return answer;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(24))); // [1, 2, 3, 4, 6, 8, 12, 24]
        System.out.println(Arrays.toString(solution(29))); // [1, 29]
    }
}
