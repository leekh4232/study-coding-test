def solution(A, B):
    B *= 2  # B 문자열을 두 번 반복하여 B에 저장

    if A in B:  # A가 B 안에 포함되어 있는지 확인
        return B.find(A)  # A가 처음 등장하는 위치 반환
    else:
        return -1  # A가 B에 포함되지 않으면 -1 반환

# 테스트 예제 실행
print(solution("hello", "ohell")) # 1
print(solution("apple", "elppa")) # -1
print(solution("atat", "tata")) # 1
print(solution("abc", "abc")) # 0