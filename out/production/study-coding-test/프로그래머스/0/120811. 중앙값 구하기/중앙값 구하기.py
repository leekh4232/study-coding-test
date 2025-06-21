def solution(array):
    array.sort()  # 주어진 리스트를 오름차순 정렬

    # 중앙값을 반환 (리스트 길이가 항상 홀수이므로 중간 인덱스 활용)
    return array[len(array) // 2]

# 테스트 예제 실행
print(solution([1, 2, 7, 10, 11]))  # 7
print(solution([9, -1, 0]))         # 0