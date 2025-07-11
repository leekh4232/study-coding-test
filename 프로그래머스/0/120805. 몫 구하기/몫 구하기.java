// Solution 클래스 정의
public class Solution {
    // solution 메서드는 두 정수를 입력받아 num1을 num2로 나눈 몫을 반환함
    public static int solution(int num1, int num2) {
        // 정수 나눗셈 연산을 수행하여 결과를 반환
        return num1 / num2;
    }

    // main 메서드는 프로그램 실행의 시작점이며 테스트를 위해 사용됨
    public static void main(String[] args) {
        System.out.println(solution(10, 5));
        System.out.println(solution(7, 2));
    }
}