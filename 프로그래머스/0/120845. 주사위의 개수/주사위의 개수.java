public class Solution {

    public static int solution(int[] box, int n) {
        int answer = 1;

        // 각 차원(가로, 세로, 높이)에 대해 반복
        for (int i = 0; i < box.length; i++) {
            answer *= box[i] / n;  // 해당 방향에서 들어갈 수 있는 주사위 개수 곱셈
        }

        return answer;  // 전체 들어갈 수 있는 주사위 개수 반환
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 1, 1}, 1));    // 1
        System.out.println(solution(new int[]{10, 8, 6}, 3));   // 12
    }
}
