// Solution 클래스 정의
class Solution {

    // solution 메서드는 num이 n의 배수일 경우 1, 아니면 0을 반환함
    public static int solution(int num, int n) {
        // num을 n으로 나눈 나머지가 0이면 배수이므로 1, 아니면 0 반환
        int answer = num % n == 0 ? 1 : 0;

        // 결과 반환
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(98, 2)); // 결과 -> 1
        System.out.println(solution(34, 3)); // 결과 -> 0
    }
}