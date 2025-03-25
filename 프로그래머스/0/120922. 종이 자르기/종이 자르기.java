// Solution 클래스 정의
public class Solution {

    // solution 메서드는 M x N 크기의 종이를 1 x 1로 자르기 위한 최소 가위질 횟수를 반환함
    public static int solution(int M, int N) {
        // 세로 방향으로 (M - 1)번 자르면 M줄 생성
        int verticalCuts = M - 1;

        // 각 세로 조각마다 가로 방향으로 (N - 1)번 자름 → M줄 모두 잘라야 하므로 M * (N - 1)
        int horizontalCuts = M * (N - 1);

        // 총 가위질 횟수는 세로 절단 + 가로 절단
        return verticalCuts + horizontalCuts;
    }

    // main 메서드는 프로그램 실행의 시작점이며 테스트를 위해 사용됨
    public static void main(String[] args) {
        // 테스트 케이스 실행 및 출력 (예시 1: 2 x 2 → 3회)
        System.out.println(solution(2, 2));

        // 테스트 케이스 실행 및 출력 (예시 2: 2 x 5 → 9회)
        System.out.println(solution(2, 5));

        // 테스트 케이스 실행 및 출력 (예시 3: 1 x 1 → 0회)
        System.out.println(solution(1, 1));
    }
}