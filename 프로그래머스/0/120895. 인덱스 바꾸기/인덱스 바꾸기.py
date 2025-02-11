def solution(my_string, num1, num2):
    answer = ''

    # 문자열을 리스트로 변환 -> 한 글자씩 리스트의 원소가 된다.
    my_list = list(my_string)

    # num1과 num2의 위치에 있는 문자를 교환
    my_list[num1], my_list[num2] = my_list[num2], my_list[num1]

    # 리스트를 문자열로 변환
    answer = "".join(my_list)

    return answer

print(solution("hello", 1, 2))          # hlelo
print(solution("I love you", 3, 6))     # I l veoyou