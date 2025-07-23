import java.util.Arrays;

public class Solution {

    public static int solution(int[] numbers) {
        // 1. 배열 정렬 (오름차순)
        Arrays.sort(numbers);

        // 2. 가장 큰 곱을 계산: 앞 2개 vs 뒤 2개
        int case1 = numbers[0] * numbers[1];  // 가장 작은 두 수 (음수일 가능성)
        int case2 = numbers[numbers.length - 1] * numbers[numbers.length - 2]; // 가장 큰 두 수

        return Math.max(case1, case2);
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 2, -3, 4, -5}));          // 15
        System.out.println(solution(new int[]{0, -31, 24, 10, 1, 9}));     // 240
        System.out.println(solution(new int[]{10, 20, 30, 5, 5, 20, 5}));  // 600
    }
}
