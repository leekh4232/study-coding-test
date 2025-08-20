func solution(slice int, n int) int {
    // 기본적으로 필요한 피자 판 수 계산
    var answer int = n / slice
    // 나머지가 있으면 한 판 추가
    if n % slice != 0 {
        answer++
    }
    // 최종적으로 필요한 피자 판 수 반환
    return answer 
}