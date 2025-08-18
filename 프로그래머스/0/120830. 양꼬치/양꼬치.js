function solution(n, k) {
    // 서비스로 제공되는 음료수 개수 (10인분당 1개)
    let freeDrinks = (n - (n % 10)) / 10;

    // 실제 결제해야 할 음료수 개수 (전체 주문 개수 - 서비스 개수)
    let paidDrinks = k - freeDrinks;

    // 양꼬치 총 가격 계산
    let totalLambCost = 12000 * n;

    // 음료수 총 가격 계산 (서비스는 제외)
    let totalDrinkCost = 2000 * paidDrinks;

    // 총 결제 금액 계산
    let totalCost = totalLambCost + totalDrinkCost;

    // 최종 결과 반환
    return totalCost;
}