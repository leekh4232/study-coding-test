func solution(hp int) int {
    var reminder int = hp % 5
    var general int = (hp - reminder) / 5
    var worker int = reminder % 3
    var soldier int = (reminder - worker) / 3
    return general + soldier + worker
}