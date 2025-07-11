import java.util.*;

public class Solution {

    // 평균 반환 시간을 최소화하는 우선순위 디스크 컨트롤러 메서드
    public static int solution(int[][] jobs) {
        // 현재 시간
        int now = 0;

        // 처리된 작업 수
        int count = 0;

        // 마지막으로 작업이 끝난 시점
        int start = -1;

        // 총 반환 시간
        int totalTime = 0;

        // 작업 대기 큐: 작업 소요시간 기준 오름차순 정렬
        PriorityQueue<int[]> heap = new PriorityQueue<>(
            (a, b) -> Integer.compare(a[1], b[1])
        );

        // jobs 배열을 리스트로 변환하여 처리
        List<int[]> jobList = Arrays.asList(jobs);
        
        // 전체 작업이 처리될 때까지 반복
        while (count < jobs.length) {
            // 현재 시점까지 요청된 작업들을 힙에 추가
            for (int[] job : jobs) {
                int request = job[0];
                int duration = job[1];

                if (start < request && request <= now) {
                    heap.offer(new int[]{request, duration});
                }
            }

            // 처리할 작업이 있다면
            if (!heap.isEmpty()) {
                // 가장 짧은 작업 소요시간을 가진 작업 꺼냄
                int[] current = heap.poll();

                // 요청 시각
                int requestTime = current[0];

                // 소요 시간
                int durationTime = current[1];

                // 작업 시작 시점 갱신
                start = now;

                // 현재 시간 증가 (작업 실행)
                now += durationTime;

                // 반환 시간 누적 (종료 시점 - 요청 시점)
                totalTime += now - requestTime;

                // 처리된 작업 수 증가
                count++;
            } else {
                // 대기 작업이 없으면 시간 증가 (idle)
                now++;
            }
        }

        // 평균 반환 시간의 정수 부분 반환
        return totalTime / jobs.length;
    }

    // 테스트 케이스 실행을 위한 main 메서드
    public static void main(String[] args) {
        int[][] jobs = {{0, 3}, {1, 9}, {3, 5}};
        System.out.println(solution(jobs)); // 출력: 8
    }
}
