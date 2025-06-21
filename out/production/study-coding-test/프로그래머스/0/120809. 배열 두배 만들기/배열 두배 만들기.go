func solution(numbers []int) []int {
    for i:=0; i<len(numbers); i++ {
        numbers[i] *= 2
    }
    
    return numbers
}