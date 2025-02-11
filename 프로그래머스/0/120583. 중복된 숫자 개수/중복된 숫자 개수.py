def solution(array, n):
    answer = 0

    # 풀이 1 - 반복문을 사용하여 카운트
    # for a in array:
    #     if a % n == 0:
    #         answer += 1

    # 풀이 2 - 리스트의 count() 함수 사용
    answer = array.count(n)

    return answer

print(solution([1, 1, 2, 3, 4, 5], 1))  # 2
print(solution([0, 2, 3, 4], 1))        # 0