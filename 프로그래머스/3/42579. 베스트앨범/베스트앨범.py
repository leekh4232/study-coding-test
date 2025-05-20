# 베스트 앨범에 들어갈 노래 고유번호 리스트를 반환하는 함수
def solution(genres, plays):
    # 최종 결과를 저장할 리스트
    answer = []

    # 장르별 총 재생수를 저장할 딕셔너리
    dic_genres = {}

    # 장르별 (고유번호, 재생수) 목록을 저장할 딕셔너리
    dic_plays = {}

    # genres와 plays를 함께 순회하며 딕셔너리 구성
    for i, (g, p) in enumerate(zip(genres, plays)):
        # 해당 장르의 총 재생 수 누적
        if g not in dic_genres:
            dic_genres[g] = p
        else:
            dic_genres[g] += p

        # 해당 장르에 (고유번호, 재생수) 추가
        if g not in dic_plays:
            dic_plays[g] = [(i, p)]
        else:
            dic_plays[g].append((i, p))

    # 장르별 총 재생수를 기준으로 장르를 정렬
    for (g, p) in sorted(dic_genres.items(), key=lambda x: x[1], reverse=True):
        # 해당 장르의 곡들을 재생수 내림차순, 고유번호 오름차순으로 정렬
        for (i, k) in sorted(dic_plays[g], key=lambda x: (-x[1], x[0]))[:2]:
            # 상위 2개의 곡 고유번호를 결과 리스트에 추가
            answer.append(i)

    # 최종 결과 반환
    return answer

# 테스트 케이스 실행
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]
