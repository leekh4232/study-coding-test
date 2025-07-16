function solution(relation) {
    const rowCount = relation.length;
    const colCount = relation[0].length;
    const candidateKeys = [];

    // 모든 가능한 속성 조합(부분집합)을 순회
    for (let mask = 1; mask < (1 << colCount); mask++) {
        // 최소성(Minimality) 검사
        // 현재 mask가 이미 찾아낸 후보 키의 상위 집합인지 확인
        if (candidateKeys.some(key => (mask & key) === key)) {
            continue;
        }

        // 유일성(Uniqueness) 검사
        const uniqueTuples = new Set();
        for (let r = 0; r < rowCount; r++) {
            let tpl = '';
            for (let j = 0; j < colCount; j++) {
                // mask의 j번째 비트가 1인지 확인
                if ((mask >> j) & 1) {
                    // 선택된 속성의 값을 쉼표로 구분하여 문자열로 조합
                    tpl += relation[r][j] + ',';
                }
            }
            uniqueTuples.add(tpl);
        }

        // Set의 크기가 전체 행의 개수와 같다면 모든 튜플이 유일
        if (uniqueTuples.size === rowCount) {
            candidateKeys.push(mask);
        }
    }

    return candidateKeys.length;
}