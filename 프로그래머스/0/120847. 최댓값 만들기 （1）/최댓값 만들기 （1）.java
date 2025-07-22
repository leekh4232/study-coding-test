public class Solution {

    public static int solution(int[] numbers) {
        int answer = 0;
        int n = numbers.length;

        // 선택 정렬 (오름차순)
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (numbers[j] < numbers[i]) {
                    // i번째 원소와 minIndex 원소를 교환
                    int temp = numbers[i];
                    numbers[i] = numbers[j];
                    numbers[j] = temp;
                }
            }
        }

        // 마지막 두 수의 곱이 최댓값
        answer = numbers[n - 1] * numbers[n - 2];

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 2, 3, 4, 5}));        // 20
        System.out.println(solution(new int[]{0, 31, 24, 10, 1, 9}));  // 744
    }
}
