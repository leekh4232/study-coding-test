function solution(n) {
    var answer = 0;
    
    for (let i = 1; i < n * 6; i++) {
        if (6 * i % n == 0) {
            answer = i;
            break;
        }
    }
    
    return answer;
}

console.log(solution(6));
console.log(solution(10));
console.log(solution(4));