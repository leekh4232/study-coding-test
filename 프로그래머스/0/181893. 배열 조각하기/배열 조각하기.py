def solution(arr, query):
    # 1. query 리스트를 순회하면서 arr을 지속적으로 잘라냄
    for i in range(len(query)):
        if i % 2 == 0:  # 짝수 인덱스 → 뒷부분 제거
            arr = arr[:query[i] + 1]
        else:  # 홀수 인덱스 → 앞부분 제거
            arr = arr[query[i]:]

    # 2. 최종적으로 남은 배열 반환
    return arr

# ✅ 예제 테스트 실행
print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))  # 결과: [1, 2, 3]
print(solution([10, 21, 32, 43, 54, 65], [4, 1, 2]))  # 결과: [21, 32, 43]