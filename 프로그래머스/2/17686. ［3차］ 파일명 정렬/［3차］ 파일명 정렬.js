function solution(files) {
    // 파일명을 HEAD, NUMBER, TAIL로 분리
    let split = files.map(f => f.match(/([^0-9]+)([0-9]+)(.*)/));

    // 정렬: HEAD(소문자 비교) → NUMBER(숫자 비교)
    split.sort((a, b) => {
        const headA = a[1].toLowerCase();
        const headB = b[1].toLowerCase();

        if (headA < headB) return -1;
        if (headA > headB) return 1;

        const numA = parseInt(a[2]);
        const numB = parseInt(b[2]);

        return numA - numB;
    });

    // 정렬된 파일명을 다시 문자열로 조합
    return split.map(parts => parts.slice(1).join(''));
}

// ✅ 예제 테스트 실행
console.log(solution([
    "img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"
]));
// 결과: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

console.log(solution([
    "F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"
]));
// 결과: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
