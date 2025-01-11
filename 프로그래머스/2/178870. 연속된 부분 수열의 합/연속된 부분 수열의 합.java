import java.util.Arrays;

/**
 * 프로그래머스 178870번 - 연속된 부분 수열의 합
 * https://school.programmers.co.kr/learn/courses/30/lessons/178870
 */
public class Solution {
    public int[] solution(int[] sequence, int k) {
        // 부분합 배열 생성
        int[] prefixSum = new int[sequence.length + 1];
        for (int i = 1; i <= sequence.length; i++) {
            prefixSum[i] = prefixSum[i - 1] + sequence[i - 1];
        }

        // 결과값 초기화
        int[] answer = new int[2];
        int minLength = Integer.MAX_VALUE;

        // 각 구간을 탐색하여 합이 k가 되는 구간 찾기
        for (int i = 0; i < sequence.length; i++) {
            for (int j = i; j < sequence.length; j++) {
                int currentSum = prefixSum[j + 1] - prefixSum[i];

                if (currentSum == k) {
                    int currentLength = j - i;
                    if (currentLength < minLength) {
                        minLength = currentLength;
                        answer[0] = i;
                        answer[1] = j;
                    }
                    break; // 부분합이 k가 되면 더 길어진 구간은 필요 없음
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] result = sol.solution(new int[]{1, 2, 3, 4, 5}, 7);
        System.out.println(Arrays.toString(result));    // [2, 3]

        result = sol.solution(new int[]{1, 1, 1, 2, 3, 4, 5}, 5);
        System.out.println(Arrays.toString(result));    // [6, 6]

        result = sol.solution(new int[]{2, 2, 2, 2, 2}, 6);
        System.out.println(Arrays.toString(result));    // [0, 2]
    }
}
