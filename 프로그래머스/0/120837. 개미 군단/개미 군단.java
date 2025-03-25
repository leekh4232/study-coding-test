// Solution 클래스 정의
public class Solution {

    // solution 메서드는 주어진 체력(hp)을 최소 병력으로 맞추기 위한 개미 수를 반환함
    public static int solution(int hp) {
        // 장군개미는 공격력 5 → 최대한 많이 사용해 체력을 깎음
        int general = hp / 5;

        // 장군개미로 처리하고 남은 체력을 계산
        int remainder = hp % 5;

        // 병정개미는 공격력 3 → 남은 체력을 병정개미로 최대한 처리
        int soldier = remainder / 3;

        // 병정개미로 처리하고 남은 체력은 일개미가 처리 (공격력 1)
        int worker = remainder % 3;

        // 사용한 개미 수의 총합을 반환
        return general + soldier + worker;
    }

    // main 메서드는 프로그램 실행의 시작점이며 테스트 케이스 실행을 위해 사용됨
    public static void main(String[] args) {
        // 테스트 케이스 실행 및 출력 (예시 1: hp = 23)
        System.out.println(solution(23));  // 출력: 5

        // 테스트 케이스 실행 및 출력 (예시 2: hp = 24)
        System.out.println(solution(24));  // 출력: 6

        // 테스트 케이스 실행 및 출력 (예시 3: hp = 999)
        System.out.println(solution(999)); // 출력: 201
    }
}