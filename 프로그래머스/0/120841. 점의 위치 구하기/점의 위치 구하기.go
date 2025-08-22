// 사분면 판별 함수
func solution(dot []int) int {
    if dot[0] > 0 && dot[1] > 0 {
        return 1
    } else if dot[0] < 0 && dot[1] > 0 {
        return 2
    } else if dot[0] < 0 && dot[1] < 0 {
        return 3
    } else if dot[0] > 0 && dot[1] < 0 {
        return 4
    }
    return 0 // 입력이 0인 경우 등 예외 처리
}