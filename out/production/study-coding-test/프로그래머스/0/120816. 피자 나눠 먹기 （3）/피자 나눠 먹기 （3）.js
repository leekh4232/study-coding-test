function solution(slice, n) {
    var answer = 0;
    
    if (n % slice == 0) {
        answer = parseInt(n / slice);
    } else {
        answer = parseInt(n / slice) + 1
    }
    
    return answer;
}