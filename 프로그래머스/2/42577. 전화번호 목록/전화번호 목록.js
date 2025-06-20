// 전화번호 목록에 접두어 관계가 있는지 확인하는 함수
function solution(phoneBook) {
    // 전화번호를 키로 저장할 해시맵 객체 생성
    const hashMap = {};

    // 모든 전화번호를 해시맵에 저장 (값은 의미 없음)
    for (const nums of phoneBook) {
        hashMap[nums] = true;
    }

    // 각 전화번호마다 접두어 검사 수행
    for (const nums of phoneBook) {
        // 접두어를 만들기 위한 문자열 초기화
        let arr = "";

        // 전화번호의 각 숫자를 앞에서부터 더해 나가며 접두어 생성
        for (const num of nums) {
            arr += num;

            // 접두어가 해시맵에 존재하고, 자기 자신은 아닐 때
            if (arr in hashMap && arr !== nums) {
                // 접두어 관계가 존재하므로 즉시 false 반환
                return false;
            }
        }
    }

    // 모든 전화번호 검사 결과 접두어 관계가 없으므로 true 반환
    return true;
}

// 테스트 케이스 실행
console.log(solution(["119", "97674223", "1195524421"])); // False
console.log(solution(["123", "456", "789"])); // True
console.log(solution(["12", "123", "1235", "567", "88"])); // False
