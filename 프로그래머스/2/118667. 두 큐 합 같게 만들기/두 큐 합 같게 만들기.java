import java.util.*;

public class Solution {
    public int solution(int[] queue1, int[] queue2) {
        // 두 큐의 합을 구함
        long sum1 = Arrays.stream(queue1).sum();
        long sum2 = Arrays.stream(queue2).sum();

        // 두 큐의 합이 같아야 하는 목표 값
        long target = (sum1 + sum2) / 2;

        // 두 큐의 합이 홀수이면 나눌 수 없으므로 -1 반환
        if ((sum1 + sum2) % 2 != 0) {
            return -1;
        }

        // 두 큐를 하나의 리스트로 합침
        int n = queue1.length;
        int[] combined = new int[queue1.length + queue2.length];
        System.arraycopy(queue1, 0, combined, 0, queue1.length);
        System.arraycopy(queue2, 0, combined, queue1.length, queue2.length);

        // 투 포인터 초기화
        int S = 0, E = n; // S는 queue1의 시작, E는 queue2의 시작

        // 현재 합을 첫 번째 큐의 합으로 초기화
        long P = sum1;

        // 최대 이동 횟수는 두 큐의 길이의 합의 두 배
        int maxMoves = 2 * combined.length;
        int moves = 0;

        // 최대 이동 횟수 내에서 반복
        while (moves < maxMoves) {
            // 현재 합이 목표 값과 같으면 이동 횟수 반환
            if (P == target) {
                return moves;
            }
            // 현재 합이 목표 값보다 작으면
            else if (P < target) {
                // 두 번째 큐에서 값을 가져와 현재 합에 더함
                P += combined[E];
                // 두 번째 큐의 다음 인덱스로 이동
                E = (E + 1) % combined.length;
            } else {
                // 현재 합이 목표 값보다 크면 첫 번째 큐에서 값을 빼줌
                P -= combined[S];
                // 첫 번째 큐의 다음 인덱스로 이동
                S = (S + 1) % combined.length;
            }
            // 이동 횟수 증가
            moves++;
        }

        // 최대 이동 횟수 내에 목표 값을 만들 수 없으면 -1 반환
        return -1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(new int[]{3, 2, 7, 2}, new int[]{4, 6, 5, 1})); // 2
        System.out.println(sol.solution(new int[]{1, 2, 1, 2}, new int[]{1, 10, 1, 2})); // 7
        System.out.println(sol.solution(new int[]{1, 1}, new int[]{1, 5})); // -1
    }
}