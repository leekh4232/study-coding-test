def solution(array):
    # 1. 배열을 오름차순 정렬
    array.sort()

    # 2. 중앙값 찾기
    # 배열 길이는 홀수이므로, 중앙값의 인덱스는 len(array) // 2
    return array[len(array) // 2]

# ✅ 예제 테스트 실행
print(solution([1, 2, 7, 10, 11]))  # 결과: 7
print(solution([9, -1, 0]))         # 결과: 0