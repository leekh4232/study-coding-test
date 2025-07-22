public class Solution {

    public static int solution(int[] common) {
        int answer = 0;

        // 등차수열인지 확인 (공차가 일정한 경우)
        if (common[1] - common[0] == common[2] - common[1]) {
            int diff = common[1] - common[0];
            answer = common[common.length - 1] + diff;
        }
        // 등비수열인지 확인 (공비가 일정한 경우)
        else if (common[1] / common[0] == common[2] / common[1]) {
            int ratio = common[1] / common[0];
            answer = common[common.length - 1] * ratio;
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 2, 3, 4}));  // 5
        System.out.println(solution(new int[]{2, 4, 8}));     // 16
    }
}