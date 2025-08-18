func solution(M int, N int) int {
    // 세로 방향으로 (M - 1)번 자르면 M줄 생성
    var verticalCuts int = M - 1;

    // 각 세로 조각마다 가로 방향으로 (N - 1)번 자름 → M줄 모두 잘라야 하므로 M * (N - 1)
    var horizontalCuts int = M * (N - 1);

    // 총 가위질 횟수는 세로 절단 + 가로 절단
    return verticalCuts + horizontalCuts;
}