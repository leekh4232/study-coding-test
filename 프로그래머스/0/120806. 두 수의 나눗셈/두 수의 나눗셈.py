def solution(num1, num2):
    # 출력 결과가 정수를 요구하므로 int()함수를 사용해야 한다.
    return int(num1 / num2 * 1000)

print(solution(3, 2))      # 결과값 : 1500
print(solution(7, 3))      # 결과값 : 2333