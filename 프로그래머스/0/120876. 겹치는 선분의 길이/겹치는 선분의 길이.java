import java.util.*;

public class Solution {
    public static int solution(int[][] lines) {
        int answer = 0;
        int[] count = new int[200];  // -100부터 100까지 총 200칸

        // 각 선분의 범위만큼 카운트 증가
        for (int[] line : lines) {
            for (int i = line[0]; i < line[1]; i++) {
                count[i + 100] += 1;  // 인덱스 보정
            }
        }

        // 두 개 이상의 선분이 겹친 부분의 개수 계산
        for (int c : count) {
            if (c == 2 || c == 3) {
                answer += 1;
            }
        }

        return answer;
    }

    // ✅ 예제 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(new int[][]{{0, 1}, {2, 5}, {3, 9}}));   // 결과: 2
        System.out.println(solution(new int[][]{{-1, 1}, {1, 3}, {3, 9}})); // 결과: 0
        System.out.println(solution(new int[][]{{0, 5}, {3, 9}, {1, 10}})); // 결과: 8
    }
}
