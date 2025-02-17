def solution(age):
    # 1. 변환된 결과를 저장할 변수 초기화
    answer = ''

    # 2. 나이를 문자열로 변환 후 각 자리 숫자를 리스트로 저장
    my_age = list(map(int, str(age)))

    # 3. 각 숫자를 대응되는 알파벳으로 변환
    for m in my_age:
        answer += chr(m + ord('a'))  # 'a'의 ASCII 코드(97) + 숫자

    # 4. 변환된 문자열 반환
    return answer

# ✅ 예제 테스트 실행
print(solution(23))   # 결과: "cd"
print(solution(51))   # 결과: "fb"
print(solution(100))  # 결과: "baa"