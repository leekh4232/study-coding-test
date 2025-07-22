public class Solution {

    public static int solution(int[] sides) {
        // 가장 짧은 변
        int shortest = Math.min(sides[0], sides[1]);

        // 가능한 경우의 수는 2 * shortest - 1
        int answer = 2 * shortest - 1;

        return answer;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 2}));   // 1
        System.out.println(solution(new int[]{3, 6}));   // 5
        System.out.println(solution(new int[]{11, 7}));  // 13
    }
}
