def solution(n, a, b):
    answer = 0

    while a != b:  # 두 참가자가 만날 때까지 반복
        a = (a + 1) // 2  # 다음 라운드의 참가자 번호 계산
        b = (b + 1) // 2  # 다음 라운드의 참가자 번호 계산
        answer += 1  # 라운드 수 증가

    return answer
