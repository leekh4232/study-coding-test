// 참가자 중 완주하지 못한 사람을 찾아 반환하는 함수
function solution(participant, completion) {
    // 이름의 해시값을 키로, 이름 자체를 값으로 저장할 객체 생성
    const hashDict = {};

    // 참가자의 해시값 총합을 저장할 변수
    let sumHash = 0;

    // 참가자 리스트를 순회하면서 해시값을 누적하고 객체에 저장
    for (const part of participant) {
        // 현재 참가자의 해시값을 계산
        const hash = hashCode(part);

        // 해시값을 키로, 참가자 이름을 값으로 저장
        hashDict[hash] = part;

        // 참가자의 해시값을 누적
        sumHash += hash;
    }

    // 완주자 리스트를 순회하면서 해시값을 총합에서 차감
    for (const comp of completion) {
        // 완주자의 해시값을 총합에서 차감
        sumHash -= hashCode(comp);
    }

    // 남은 해시값은 완주하지 못한 사람의 해시값
    // 이를 통해 해당 이름을 객체에서 찾아 반환
    return hashDict[sumHash];
}

// 문자열을 해시값으로 변환하는 함수 (JavaScript용 해시 구현)
function hashCode(str) {
    // 해시 초기값 설정
    let hash = 0;

    // 문자열을 한 글자씩 순회하면서 해시 계산
    for (let i = 0; i < str.length; i++) {
        const char = str.charCodeAt(i);
        hash = (hash * 31 + char) | 0; // 32비트 정수로 변환
    }

    return hash;
}

// 테스트 케이스 실행
console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"]));
// --> leo

console.log(solution(
    ["marina", "josipa", "nikola", "vinko", "filipa"],
    ["josipa", "filipa", "marina", "nikola"]
));
// --> vinko

console.log(solution(
    ["mislav", "stanko", "mislav", "ana"],
    ["stanko", "ana", "mislav"]
));
// --> mislav