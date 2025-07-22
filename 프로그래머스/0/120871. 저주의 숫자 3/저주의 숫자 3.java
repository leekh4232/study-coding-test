public class Solution {

    public static int solution(int n) {
        int answer = 0;

        for (int count = 0; count < n; count++) {
            answer++;

            // 3의 배수이거나 숫자에 3이 포함되면 다음 숫자로 넘김
            while (answer % 3 == 0 || String.valueOf(answer).contains("3")) {
                answer++;
            }
        }

        return answer;
    }

    // ✅ 테스트 실행
    public static void main(String[] args) {
        System.out.println(solution(15));  // 출력: 25
        System.out.println(solution(40));  // 출력: 76
    }
}
