function solution(files) {
    // 각 파일명을 정규표현식으로 세 부분(HEAD, NUMBER, TAIL)으로 분리
    // match 결과: [전체문자열, HEAD, NUMBER, TAIL]
    let split = files.map(f => f.match(/([^0-9]+)([0-9]+)(.*)/));
    console.log(split);

    // 정렬 기준 정의
    // 1. HEAD는 소문자로 변환하여 사전순 비교
    // 2. HEAD가 같으면 NUMBER를 정수로 변환하여 오름차순 비교
    split.sort((a, b) => {
        const headA = a[1].toLowerCase();
        const headB = b[1].toLowerCase();

        // HEAD 기준 정렬
        if (headA < headB) return -1;
        if (headA > headB) return 1;

        // HEAD가 같을 경우 NUMBER 기준 정렬
        const numA = parseInt(a[2]);
        const numB = parseInt(b[2]);

        return numA - numB;
    });

    // 정렬된 결과를 다시 파일명 문자열로 합쳐서 반환
    return split.map(parts => parts.slice(1).join(''));
}

// ✅ 예제 테스트 실행
console.log(solution([
    "img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"
]));
// 출력 결과: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

console.log(solution([
    "F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"
]));
// 출력 결과: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
