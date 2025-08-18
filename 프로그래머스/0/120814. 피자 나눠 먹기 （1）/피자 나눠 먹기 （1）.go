func solution(n int) int {
    var answer int = n / 7 // 7로 나눈 몫을 기본 피자 판 수로 설정

    if n % 7 > 0 { // 나머지가 있는 경우 (즉, 추가 피자가 필요한 경우)
        answer++ // 피자 한 판을 추가
    }

    return answer // 계산된 피자 판 수 반환
}