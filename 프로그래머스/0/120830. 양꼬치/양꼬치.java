public class Solution {

    // solution 메서드는 양꼬치 n인분과 음료수 k개를 먹었을 때의 총 결제 금액을 반환함
    public static int solution(int n, int k) {
        // 서비스로 제공되는 음료수 개수 (10인분당 1개)
        int freeDrinks = n / 10;

        // 실제 결제해야 할 음료수 개수 (전체 주문 개수 - 서비스 개수)
        int paidDrinks = k - freeDrinks;

        // 양꼬치 총 가격 계산
        int totalLambCost = 12000 * n;

        // 음료수 총 가격 계산 (서비스는 제외)
        int totalDrinkCost = 2000 * paidDrinks;

        // 총 결제 금액 계산
        int totalCost = totalLambCost + totalDrinkCost;

        // 최종 결과 반환
        return totalCost;
    }

    // main 메서드는 프로그램 실행의 시작점이며 테스트를 위해 작성됨
    public static void main(String[] args) {
        // solution 메서드를 호출하여 결과 출력 (예시 1: 10인분, 음료 3개)
        System.out.println(solution(10, 3));

        // solution 메서드를 호출하여 결과 출력 (예시 2: 64인분, 음료 6개)
        System.out.println(solution(64, 6));
    }
}