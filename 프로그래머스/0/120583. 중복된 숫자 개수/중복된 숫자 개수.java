public class Solution {

    public static int solution(int[] array, int n) {
        int answer = 0; // n이 등장하는 횟수를 저장할 변수

        for (int i = 0; i < array.length; i++) {
            if (array[i] == n) {
                answer++; // 등장 횟수 증가
            }
        }

        return answer; // 등장한 횟수 반환
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 1, 2, 3, 4, 5}, 1)); // 2
        System.out.println(solution(new int[]{0, 2, 3, 4}, 1));       // 0
    }
}
