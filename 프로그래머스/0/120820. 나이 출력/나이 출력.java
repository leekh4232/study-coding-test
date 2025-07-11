// Solution 클래스 정의
public class Solution {

    // solution 메서드는 나이를 입력받아 출생 연도를 반환함
    public static int solution(int age) {
        // 출생 연도는 2022년에서 나이를 뺀 후, 태어난 해에 1살이므로 +1을 더함
        int answer = 2022 - age + 1;

        // 계산된 출생 연도를 반환
        return answer;
    }

    // main 메서드는 프로그램 실행의 시작점이며 테스트를 위해 작성됨
    public static void main(String[] args) {
        // solution 메서드를 호출하여 결과 출력 (예시 1: age = 40 → 1983년생)
        System.out.println(solution(40));

        // solution 메서드를 호출하여 결과 출력 (예시 2: age = 23 → 2000년생)
        System.out.println(solution(23));
    }
}
