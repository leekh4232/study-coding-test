def solution(my_string, num1, num2):
    my_list = list(my_string)  # 문자열을 리스트로 변환

    # num1과 num2의 위치에 있는 문자를 교환
    my_list[num1], my_list[num2] = my_list[num2], my_list[num1]

    return "".join(my_list)  # 리스트를 다시 문자열로 변환하여 반환

# 테스트 예제 실행
print(solution("hello", 1, 2))          # "hlelo"
print(solution("I love you", 3, 6))     # "I l veoyou"
