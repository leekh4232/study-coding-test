def solution(my_string):
    # 문자열을 공백 기준으로 잘라서 리스트로 변환 --> ["3", "+", "4"]
    my_list = my_string.split()

    # 리스트의 첫 번째 요소를 정수로 변환하여 answer에 저장
    answer = int(my_list[0])

    # 리스트의 두 번째 요소부터 마지막 요소까지 반복
    # 연산자, 숫자, 연산자, 숫자 ... 의 순서이므로 1부터 시작하여 2씩 증가
    for i in range(1, len(my_list)-1, 2):
        # 연산자가 "+"인 경우에는 다음 숫자를 더하고
        if my_list[i] == '+':
            answer += int(my_list[i+1])
        # 연산자가 "-"인 경우에는 다음 숫자를 뺀다.
        else:
            answer -= int(my_list[i+1])

    return answer

print(solution("3 + 4"))    # 7

# 프로그래머스에서 제시하지 않는 또 다른 테스트 케이스
print(solution("5 + 7 - 2 - 5 + 10")) # 15