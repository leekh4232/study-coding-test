import java.util.Arrays;

public class Solution {
    public int[] solution(int[] sequence, int k) {
        int left = 0, right = 0; // 투 포인터 초기화
        int currentSum = sequence[0]; // 현재 부분합 초기화
        int minLength = Integer.MAX_VALUE; // 최소 길이를 무한대로 초기화
        int[] answer = new int[2]; // 정답 저장 배열

        while (right < sequence.length) { // 오른쪽 포인터가 범위를 벗어나지 않도록 설정
            if (currentSum == k) { // 부분합이 k와 같을 경우
                int currentLength = right - left; // 현재 부분 수열의 길이 계산
                if (currentLength < minLength) { // 최소 길이 갱신
                    minLength = currentLength;
                    answer[0] = left;
                    answer[1] = right;
                }
                currentSum -= sequence[left]; // 왼쪽 포인터 이동을 위해 값 제거
                left++; // 왼쪽 포인터 증가
            } else if (currentSum < k) { // 부분합이 k보다 작다면
                right++; // 오른쪽 포인터 이동
                if (right < sequence.length) { // 배열 범위 체크 후 값 추가
                    currentSum += sequence[right];
                }
            } else { // 부분합이 k보다 크다면
                currentSum -= sequence[left]; // 왼쪽 포인터 이동을 위해 값 제거
                left++; // 왼쪽 포인터 증가
            }
        }

        return answer; // 결과 반환
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 테스트 케이스 실행
        System.out.println(Arrays.toString(sol.solution(new int[]{1, 2, 3, 4, 5}, 7))); // [2, 3]
        System.out.println(Arrays.toString(sol.solution(new int[]{1, 1, 1, 2, 3, 4, 5}, 5))); // [6, 6]
        System.out.println(Arrays.toString(sol.solution(new int[]{2, 2, 2, 2, 2}, 6))); // [0, 2]
    }
}
