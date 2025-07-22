public class Solution {

    public static int[] solution(String[] strlist) {
        int[] answer = new int[strlist.length];

        // 각 문자열의 길이를 배열에 저장
        for (int i = 0; i < strlist.length; i++) {
            answer[i] = strlist[i].length();
        }

        return answer;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        String[] input1 = {"We", "are", "the", "world!"};
        String[] input2 = {"I", "Love", "Programmers."};

        System.out.println(java.util.Arrays.toString(solution(input1))); // [2, 3, 3, 6]
        System.out.println(java.util.Arrays.toString(solution(input2))); // [1, 4, 12]
    }
}
