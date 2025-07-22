public class Solution {

    public static int solution(String[] s1, String[] s2) {
        int answer = 0;

        for (int i = 0; i < s1.length; i++) {
            for (int j = 0; j < s2.length; j++) {
                if (s1[i].equals(s2[j])) {
                    answer++;
                    break; // 중복 방지를 위해 바로 탈출
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(
            new String[]{"a", "b", "c"},
            new String[]{"com", "b", "d", "p", "c"}
        )); // 2

        System.out.println(solution(
            new String[]{"n", "omg"},
            new String[]{"m", "dot"}
        )); // 0
    }
}