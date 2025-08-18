func solution(n int) int {
    fact := 1 // 팩토리얼 값을 저장할 변수 초기화
    i := 1    // i값을 1부터 시작
    for fact <= n { // fact가 n을 초과하기 전까지 반복
        i++ // i를 증가
        fact *= i // fact에 i를 곱하여 팩토리얼 값을 계산
    }
    return i - 1 // 초과하기 전의 최대 i 값 반환
}