import java.util.*;

public class Solution {

    // 기능이 배포되는 개수를 계산하는 메서드
    public static int[] solution(int[] progresses, int[] speeds) {
        // 작업의 완료 일수를 저장할 큐
        Queue<Integer> queue = new LinkedList<>();
        
        // 각 작업이 완료되는 데 필요한 일수 계산
        for (int i = 0; i < progresses.length; i++) {
            // 올림 계산을 위해 Math.ceil 사용
            int days = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
            queue.add(days);
        }

        // 결과를 저장할 리스트
        List<Integer> answerList = new ArrayList<>();

        while (!queue.isEmpty()) {
            // 첫 번째 작업의 배포 기준일
            int deployDay = queue.poll();
            int count = 1; // 배포되는 기능 개수

            // 기준일보다 작거나 같은 작업들은 함께 배포
            while (!queue.isEmpty() && queue.peek() <= deployDay) {
                queue.poll();
                count++;
            }

            // 배포 개수를 리스트에 추가
            answerList.add(count);
        }

        // 리스트를 int 배열로 변환하여 반환
        return answerList.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        // ✅ 예제 테스트 실행
        System.out.println(Arrays.toString(solution(new int[]{93, 30, 55}, new int[]{1, 30, 5}))); // [2, 1]
        System.out.println(Arrays.toString(solution(new int[]{95, 90, 99, 99, 80, 99}, new int[]{1, 1, 1, 1, 1, 1}))); // [1, 3, 2]
    }
}
