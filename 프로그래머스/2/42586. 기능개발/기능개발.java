/**
 * 프로그래머스 42586번 - 기능개발
 * https://school.programmers.co.kr/learn/courses/30/lessons/42586
 */
import java.util.*;

public class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Queue<Integer> days = new LinkedList<>();

        // 각 작업의 남은 일수를 계산하여 큐에 추가
        for (int i = 0; i < progresses.length; i++) {
            int d = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
            days.add(d);
        }

        int cnt = 1; // 완료된 기능 수
        int prev = days.poll(); // 첫 번째 작업의 소요 일수

        while (!days.isEmpty()) {
            int cur = days.poll();
            if (prev >= cur) {
                cnt++; // 이전 작업과 함께 배포 가능
            } else {
                answer.add(cnt); // 이전 작업까지 배포 완료
                cnt = 1; // 현재 작업부터 새로운 배포 시작
                prev = cur; // 새로운 기준 업데이트
            }
        }

        // 마지막 배포 그룹 추가
        answer.add(cnt);

        // List<Integer>를 int[]로 변환
        return answer.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        Solution ex = new Solution();

        int[] progresses1 = {93, 30, 55};
        int[] speeds1 = {1, 30, 5};
        System.out.println(Arrays.toString(ex.solution(progresses1, speeds1))); // [2, 1]

        int[] progresses2 = {95, 90, 99, 99, 80, 99};
        int[] speeds2 = {1, 1, 1, 1, 1, 1};
        System.out.println(Arrays.toString(ex.solution(progresses2, speeds2))); // [1, 3, 2]
    }
}