// Solution 클래스 정의
public class Solution {

    // solution 메서드는 두 정수를 입력받아 첫 번째에서 두 번째를 뺀 값을 반환함
    public static int solution(int num1, int num2) {
        // num1에서 num2를 뺀 결과를 answer 변수에 저장
        int answer = num1 - num2;

        // answer 값을 반환
        return answer;
    }

    // main 메서드는 프로그램 실행의 시작점이며 테스트를 위해 작성됨
    public static void main(String args[]) {
        // solution 메서드를 호출하여 결과를 출력 (예시 1: 2 - 3)
        System.out.println(solution(2, 3));     // 결과값: -1

        // solution 메서드를 호출하여 결과를 출력 (예시 2: 100 - 2)
        System.out.println(solution(100, 2));   // 결과값: 98
    }
}
