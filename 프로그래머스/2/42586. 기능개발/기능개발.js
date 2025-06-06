function solution(progresses, speeds) {
    // 진행도와 속도를 배열로 복사 (원본 보존)
    progresses = [...progresses];
    speeds = [...speeds];

    // 결과를 저장할 배열
    const answer = [];

    // 현재 날짜 (경과 일수)
    let days = 0;

    // 현재 배포에 포함될 기능 개수
    let cnt = 0;

    // 모든 작업이 끝날 때까지 반복
    while (progresses.length) {
        // 현재 작업이 완료되었는지 확인
        if (progresses[0] + days * speeds[0] >= 100) {
            // 완료된 작업 제거
            progresses.shift();
            speeds.shift();
            // 배포 대기 중인 기능 개수 증가
            cnt += 1;
        } else {
            // 아직 완료되지 않은 작업이 나왔을 경우
            if (cnt > 0) {
                // 지금까지 완료된 기능들을 한 번에 배포
                answer.push(cnt);
                cnt = 0;
            }
            // 하루 경과
            days += 1;
        }
    }

    // 마지막에 남아 있는 배포 대기 기능이 있다면 추가
    answer.push(cnt);

    // 결과 반환
    return answer;
}

// ✅ 테스트 예제 실행
console.log(solution([93, 30, 55], [1, 30, 5]));          // [2, 1]
console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]));  // [1, 3, 2]
