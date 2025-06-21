def solution(arr, divisor):
    # 1. 나누어 떨어지는 원소를 저장할 리스트
    result = []

    # 2. 배열을 순회하면서 divisor로 나누어 떨어지는 숫자만 선택
    for num in arr:
        if num % divisor == 0:
            result.append(num)

    # 3. 결과 리스트가 비어 있다면 [-1] 반환
    if not result:
        return [-1]

    # 4. 결과를 오름차순 정렬하여 반환
    result.sort()

    return result

# ✅ 예제 테스트 실행
if __name__ == '__main__':
    print(solution([5, 9, 7, 10], 5))   # 결과: [5, 10]
    print(solution([2, 36, 1, 3], 1))   # 결과: [1, 2, 3, 36]
    print(solution([3, 2, 6], 10))      # 결과: [-1]
    print(solution([3, 2, 6], 2))       # 결과: [2, 6]