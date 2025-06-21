def solution(n):
    answer = []  # 홀수를 저장할 리스트

    for i in range(1, n+1, 2):  # 1부터 n까지 2씩 증가 (홀수만 선택)
        answer.append(i)  # 홀수를 리스트에 추가

    return answer  # 생성된 홀수 리스트 반환

# 테스트 예제 실행
print(solution(10))  # [1, 3, 5, 7, 9]
print(solution(15))  # [1, 3, 5, 7, 9, 11, 13, 15]