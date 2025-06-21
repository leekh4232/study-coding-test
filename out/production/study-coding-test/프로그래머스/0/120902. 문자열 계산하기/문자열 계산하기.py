def solution(my_string):
    # 문자열을 공백 기준으로 분리하여 리스트로 변환
    my_list = my_string.split()  

    # 첫 번째 숫자를 정수로 변환하여 초기값으로 설정
    answer = int(my_list[0])

    # 1부터 2씩 증가하면서 연산자와 숫자를 순차적으로 처리
    for i in range(1, len(my_list) - 1, 2):
        if my_list[i] == '+':  # "+" 연산자이면 다음 숫자를 더함
            answer += int(my_list[i+1])
        else:  # "-" 연산자이면 다음 숫자를 뺌
            answer -= int(my_list[i+1])

    return answer  # 계산된 최종 결과 반환

# 테스트 예제 실행
print(solution("3 + 4"))    # 7
print(solution("5 + 7 - 2 - 5 + 10")) # 15
