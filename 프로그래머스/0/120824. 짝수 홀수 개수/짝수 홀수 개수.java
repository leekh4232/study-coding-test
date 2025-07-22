public class Solution {

    public static int[] solution(int[] numList) {
        int[] answer = new int[2];  // answer[0]: 짝수 개수, answer[1]: 홀수 개수

        for (int i = 0; i < numList.length; i++) {
            int n = numList[i];
            answer[n % 2]++;  // n % 2가 0이면 짝수 → answer[0], 1이면 홀수 → answer[1]
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] result1 = solution(new int[]{1, 2, 3, 4, 5});
        System.out.println("[" + result1[0] + ", " + result1[1] + "]");  // [2, 3]

        int[] result2 = solution(new int[]{1, 3, 5, 7});
        System.out.println("[" + result2[0] + ", " + result2[1] + "]");  // [0, 4]
    }
}
