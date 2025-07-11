def solution(emergency):
    # 응급도를 내림차순으로 정렬하여 순위 기준 생성
    sorted_em = sorted(emergency, reverse=True)

    # 진료 순서를 저장할 리스트 초기화
    answer = []

    # 원래 리스트의 각 요소가 정렬된 리스트에서 몇 번째인지 찾기
    for e in emergency:
        answer.append(sorted_em.index(e) + 1)

    # 최종적으로 순위 리스트 반환
    return answer

# ✅ 예제 테스트 실행
print(solution([3, 76, 24]))
# 결과: [3, 1, 2] (76이 1등, 24가 2등, 3이 3등)

print(solution([1, 2, 3, 4, 5, 6, 7]))
# 결과: [7, 6, 5, 4, 3, 2, 1] (큰 숫자가 높은 순위)

print(solution([30, 10, 23, 6, 100]))
# 결과: [2, 4, 3, 5, 1] (100이 1등, 30이 2등, 23이 3등...)