public class Solution {
    public static String solution(String bin1, String bin2) {
        // 이진수를 10진수로 변환
        int a = Integer.parseInt(bin1, 2);
        int b = Integer.parseInt(bin2, 2);

        // 두 수를 더한 후 다시 이진수 문자열로 변환
        String answer = Integer.toBinaryString(a + b);

        return answer;
    }

    // ✅ 예제 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution("10", "11"));     // 결과: "101"
        System.out.println(solution("1001", "1111")); // 결과: "11000"
    }
}
