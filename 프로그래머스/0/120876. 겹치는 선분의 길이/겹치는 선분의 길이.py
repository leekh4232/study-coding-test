def solution(lines):
    answer = 0
    count = [0] * 200  # -100부터 100까지 총 200칸을 저장하기 위한 배열

    # 각 선분의 범위만큼 카운트 증가
    for line in lines:
        for i in range(line[0], line[1]):  # 시작점부터 끝점-1까지
            count[i + 100] += 1  # -100을 보정하여 배열의 인덱스를 맞춤

    # 두 개 이상의 선분이 겹친 부분의 개수 계산
    answer += count.count(2)  # 두 개 이상 겹친 부분
    answer += count.count(3)  # 세 개 이상 겹친 부분

    return answer

# ✅ 예제 테스트 실행
print(solution([[0, 1], [2, 5], [3, 9]]))  # 결과값: 2
print(solution([[-1, 1], [1, 3], [3, 9]]))  # 결과값: 0
print(solution([[0, 5], [3, 9], [1, 10]]))  # 결과값: 8
