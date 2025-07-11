// Solution 클래스 정의
public class Solution {

    // solution 메서드는 두 정수를 입력받아 num1을 num2로 나눈 나머지를 반환함
    public static int solution(int num1, int num2) {
        // 나머지 연산자(%)를 이용해 num1을 num2로 나눈 나머지를 계산하여 반환
        return num1 % num2;
    }

    // main 메서드는 프로그램 실행의 시작점이며 테스트를 위해 작성됨
    public static void main(String[] args) {
        // solution 메서드를 호출하여 결과 출력 (예시 1: 3 % 2)
        System.out.println(solution(3, 2));

        // solution 메서드를 호출하여 결과 출력 (예시 2: 10 % 5)
        System.out.println(solution(10, 5));
    }
}
