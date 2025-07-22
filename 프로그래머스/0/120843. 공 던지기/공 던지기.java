import java.util.Arrays;

public class Solution {

    public static int solution(int[] numbers, int k) {
        int answer = 0;
        int p = 0;  // 현재 공을 가진 사람의 인덱스

        for (int i = 0; i < k; i++) {
            answer = numbers[p];  // 현재 공을 가진 사람의 번호 저장
            p = (p + 2) % numbers.length;  // 오른쪽으로 한 명 건너뛰고 던짐
        }

        return answer;  // k번째로 공을 던지는 사람의 번호 반환
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 2, 3, 4}, 2));        // 3
        System.out.println(solution(new int[]{1, 2, 3, 4, 5, 6}, 5));  // 3
    }
}