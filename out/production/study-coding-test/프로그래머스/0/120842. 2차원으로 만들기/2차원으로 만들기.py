def solution(num_list, n):
    # 2차원 배열을 저장할 리스트 초기화
    answer = []

    # num_list를 n개씩 잘라서 새로운 리스트에 추가
    for i in range(len(num_list) // n):
        answer.append(num_list[n * i : n * (i + 1)])

    # 최종적으로 변환된 2차원 리스트 반환
    return answer

# ✅ 예제 테스트 실행
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
# 결과: [[1, 2], [3, 4], [5, 6], [7, 8], [9]]

print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))
# 결과: [[100, 95, 2], [4, 5, 6], [18, 33, 948]]