"""
프로그래머스 12910번 - 나누어 떨어지는 숫자 배열

https://school.programmers.co.kr/learn/courses/30/lessons/12910
"""
# solution.py
def solution(arr, divisor):
    # [풀이1] 나누어 떨어지는 숫자 필터링
    # result = []

    # # arr이 [5, 9, 7, 10]일 때 num은 5, 9, 7, 10이 됨
    # for num in arr:
    #     # num이 5, 9, 7, 10일 때 divisor로 나누어 떨어지는지 확인
    #     if num % divisor == 0:
    #         result.append(num)

    # # 결과 반환, 비어있으면 [-1] 반환
    # if not result:
    #     return [-1]

    # # 결과 정렬
    # result.sort()

    # return result

    # [풀이2] 나누어 떨어지는 숫자 필터링 (람다식 버전)
    result = [num for num in arr if num % divisor == 0]
    # 결과 반환, 비어있으면 [-1] 반환
    if not result:
        return [-1]
    # 결과 정렬
    result.sort()
    return result

if __name__ == '__main__':
    print(solution([1, 5, 9, 7, 10], 5))   # [5, 10]
    print(solution([2, 36, 1, 3], 1))   # [1, 2, 3, 36]
    print(solution([3, 2, 6], 10))      # [-1]
    print(solution([3, 2, 6], 2))       # [2, 6]