import java.util.*;

public class Solution {

    public static int[] solution(int[][] score) {
        int n = score.length;
        double[] avg = new double[n];        // 각 학생의 평균 점수
        double[] sorted = new double[n];     // 정렬용 복사 배열

        // 평균 계산
        for (int i = 0; i < n; i++) {
            avg[i] = (score[i][0] + score[i][1]) / 2.0;
            sorted[i] = avg[i];  // 복사
        }

        // 내림차순 정렬
        Arrays.sort(sorted);
        for (int i = 0; i < n / 2; i++) {
            double temp = sorted[i];
            sorted[i] = sorted[n - 1 - i];
            sorted[n - 1 - i] = temp;
        }

        // 등수 계산
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            // 첫 번째로 등장한 index + 1 → 등수
            for (int j = 0; j < n; j++) {
                if (avg[i] == sorted[j]) {
                    answer[i] = j + 1;
                    break;
                }
            }
        }

        return answer;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        int[][] test1 = {{80, 70}, {90, 50}, {40, 70}, {50, 80}};
        int[][] test2 = {{80, 70}, {70, 80}, {30, 50}, {90, 100}, {100, 90}, {100, 100}, {10, 30}};

        System.out.println(Arrays.toString(solution(test1))); // [1, 2, 4, 3]
        System.out.println(Arrays.toString(solution(test2))); // [4, 4, 6, 2, 2, 1, 7]
    }
}
