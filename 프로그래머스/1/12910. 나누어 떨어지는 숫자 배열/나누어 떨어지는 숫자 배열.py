def solution(arr, divisor):
    # 나누어 떨어지는 숫자 필터링
    result = []
    for num in arr:
        if num % divisor == 0:
            result.append(num)
    # 결과 정렬
    result.sort()
    # 결과 반환, 비어있으면 [-1] 반환
    if not result:
        return [-1]
    return result