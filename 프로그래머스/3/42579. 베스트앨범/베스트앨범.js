// 베스트 앨범에 들어갈 노래 고유번호 리스트를 반환하는 함수
function solution(genres, plays) {
    // 최종 결과를 저장할 배열
    const answer = [];

    // 장르별 총 재생수를 저장할 객체
    const dicGenres = {};

    // 장르별 (고유번호, 재생수) 목록을 저장할 객체
    const dicPlays = {};

    // genres와 plays를 함께 순회하며 객체 구성
    for (let i = 0; i < genres.length; i++) {
        const g = genres[i];
        const p = plays[i];

        // 해당 장르의 총 재생 수 누적
        if (!(g in dicGenres)) {
            dicGenres[g] = p;
        } else {
            dicGenres[g] += p;
        }

        // 해당 장르에 (고유번호, 재생수) 추가
        if (!(g in dicPlays)) {
            dicPlays[g] = [[i, p]];
        } else {
            dicPlays[g].push([i, p]);
        }
    }

    // 장르별 총 재생수를 기준으로 장르를 정렬
    const sortedGenres = Object.entries(dicGenres)
        .sort((a, b) => b[1] - a[1]);

    // 정렬된 장르 리스트를 순회
    for (const [g, _] of sortedGenres) {
        // 해당 장르의 곡들을 재생수 내림차순, 고유번호 오름차순으로 정렬
        const sortedSongs = dicPlays[g].sort((a, b) => {
            if (b[1] !== a[1]) {
                return b[1] - a[1];  // 재생수 내림차순
            }
            return a[0] - b[0];      // 고유번호 오름차순
        });

        // 상위 2개의 곡 고유번호를 결과 배열에 추가
        for (let i = 0; i < Math.min(2, sortedSongs.length); i++) {
            answer.push(sortedSongs[i][0]);
        }
    }

    // 최종 결과 반환
    return answer;
}

// 테스트 케이스 실행
console.log(solution(["classic", "pop", "classic", "classic", "pop"],
            [500, 600, 150, 800, 2500])); // [4, 1, 3, 0]