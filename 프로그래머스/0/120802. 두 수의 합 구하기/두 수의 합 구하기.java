// Solution 클래스 정의
public class Solution {
    // solution 메서드는 두 정수를 입력받아 그 합을 반환함
    public static int solution(int num1, int num2) {
        // num1과 num2를 더한 값을 answer 변수에 저장
        int answer = num1 + num2;

        // answer 값을 반환
        return answer;
    }

    // main 메서드는 프로그램 실행의 시작점이며 테스트를 위해 작성됨
    public static void main(String[] args) {
        // solution 메서드를 호출하여 결과를 출력 (예시 1: 2 + 3)
        System.out.println(solution(2, 3));

        // solution 메서드를 호출하여 결과를 출력 (예시 2: 100 + 2)
        System.out.println(solution(100, 2));
    }
}
