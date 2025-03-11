import java.util.*;

class Solution {
    public int[] solution(int[] sequence, int k) {
        // 두 개의 포인터를 0으로 초기화
        int S = 0, E = 0;

        // 현재 부분합을 첫 번째 원소로 초기화
        int P = sequence[0];

        // 최소 길이를 무한대로 설정
        int minLength = Integer.MAX_VALUE;

        // 결과 저장 배열
        int[] answer = new int[2];

        // 오른쪽 포인터가 수열 범위를 넘지 않도록 설정
        while (E < sequence.length) {
            // 부분합이 k보다 작다면
            if (P < k) {
                // 오른쪽 포인터 이동
                E++;

                // 범위를 벗어나지 않도록 확인
                if (E < sequence.length) {
                    // 새로운 값 추가
                    P += sequence[E];
                }
            }
            // 부분합이 k보다 크다면
            else if (P > k) {
                // 왼쪽 포인터 이동을 위해 값 제거
                P -= sequence[S];

                // 왼쪽 포인터 증가
                S++;
            }
            // 부분합이 k와 같을 경우
            else {
                // 현재 부분 수열의 길이 계산
                int currentLength = E - S;

                // 최소 길이 갱신 조건 확인
                if (currentLength < minLength) {
                    // 최소 길이 갱신
                    minLength = currentLength;

                    // 현재 인덱스 저장
                    answer[0] = S;
                    answer[1] = E;
                }

                // 왼쪽 포인터 이동을 위해 값 제거
                P -= sequence[S];

                // 왼쪽 포인터 증가
                S++;
            }
        }

        // 찾은 부분 수열의 시작 인덱스와 끝 인덱스 반환
        return answer;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(Arrays.toString(sol.solution(new int[]{1, 2, 3, 4, 5}, 7))); // [2, 3]
        System.out.println(Arrays.toString(sol.solution(new int[]{1, 1, 1, 2, 3, 4, 5}, 5))); // [6, 6]
        System.out.println(Arrays.toString(sol.solution(new int[]{2, 2, 2, 2, 2}, 6))); // [0, 2]
    }
}