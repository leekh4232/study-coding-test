function solution(s, m) {
    let answer = "";

    if (s <= 1023) {
        answer = "No thanks";
    } else {
        let need = s - 1023;
        if ((need & m) === need) {
            answer = "Thanks";
        } else {
            answer = "Impossible";
        }
    }

    return answer;
}

// 테스트
console.log(solution(1023, 12));  // "No thanks"
console.log(solution(1024, 1));   // "Thanks"
console.log(solution(1024, 2));   // "Impossible"