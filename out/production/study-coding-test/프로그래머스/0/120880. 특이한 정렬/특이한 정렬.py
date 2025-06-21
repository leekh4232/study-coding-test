def solution(numlist, n):
    length = len(numlist)

    # 선택 정렬 수행
    for i in range(length - 1):
        min_idx = i  # 현재 위치를 최소값 인덱스로 설정

        for j in range(i + 1, length):
            if (abs(numlist[j] - n), -numlist[j]) < (
                abs(numlist[min_idx] - n), -numlist[min_idx]):
                min_idx = j  # 최소값 인덱스 갱신

        numlist[i], numlist[min_idx] = numlist[min_idx], numlist[i]  # 위치 변경

    return numlist

# ✅ 예제 테스트 실행
print(solution([1, 2, 3, 4, 5, 6], 4))
# 결과 [4, 5, 3, 6, 2, 1]

print(solution([10000, 20, 36, 47, 40, 6, 10, 7000], 30))
# 결과 [36, 40, 20, 47, 10, 6, 7000, 10000]