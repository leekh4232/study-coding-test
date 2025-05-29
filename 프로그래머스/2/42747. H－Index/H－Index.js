function solution(citations) {
    // 인용 횟수를 내림차순으로 정렬
    // 가장 많이 인용된 논문부터 비교하기 위함
    citations.sort((a, b) => b - a);

    // H-Index 결과를 저장할 변수 초기화
    let answer = 0;

    // 정렬된 인용 배열을 앞에서부터 순회
    for (let i = 0; i < citations.length; i++) {
        // 현재 논문이 i+1번 이상 인용되었는지 확인
        // 조건을 만족하면 H-Index 후보로 고려
        if (citations[i] >= i + 1) {
            answer = i + 1; // 조건 만족하므로 H-Index 갱신
        } else {
            break; // 조건을 만족하지 않으면 순회 종료
        }
    }

    // 최종적으로 계산된 H-Index 반환
    return answer;
}

// ✅ 예제 테스트 실행
console.log(solution([3, 0, 6, 1, 5]));
// 출력 결과: 3
