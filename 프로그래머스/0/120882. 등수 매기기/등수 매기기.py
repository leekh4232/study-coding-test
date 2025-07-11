def solution(score):
    # 각 학생의 평균 점수를 계산
    avg = []  # 평균 점수를 저장할 리스트
    for i in score:
        # 각 학생의 점수를 더한 후 2로 나누어 평균 계산
        avg.append(sum(i) / 2)

    # 평균 점수를 내림차순으로 정렬
    s_avg = sorted(avg, reverse=True)

    answer = []  # 등수를 저장할 리스트
    for i in avg:
        # 정렬된 리스트에서 인덱스를 찾아 등수 부여
        answer.append(s_avg.index(i) + 1)

    return answer  # 등수 리스트 반환

# 테스트 코드 실행
print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
# 결과: [1, 2, 4, 3]

print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
# 결과: [4, 4, 6, 2, 2, 1, 7]