func solution(numer1 int, denom1 int, numer2 int, denom2 int) [2]int {
    
    var numer3 int = denom2 * numer1 + numer2 * denom1
    var denom3 int = denom1 * denom2
    
    var i int = numer3
    
    for ;i > 0; i-- {
        if (numer3 % i == 0 && denom3 % i == 0) {
            break
        }
    }
    
    var result [2]int
    result[0] = numer3 / i
    result[1] = denom3 / i
    
    return result
}