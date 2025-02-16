def solution(num, total):
    # 1. 연속된 수의 첫 번째 값을 구함
    s = total // num - ((num - 1) // 2)

    # 2. 연속된 숫자들을 리스트에 저장
    answer = []
    for i in range(num):
        answer.append(s)
        s += 1  # 다음 숫자로 증가

    # 3. 결과 반환
    return answer

# ✅ 예제 테스트 실행
print(solution(3, 12))  # 결과: [3, 4, 5]
print(solution(5, 15))  # 결과: [1, 2, 3, 4, 5]
print(solution(4, 14))  # 결과: [2, 3, 4, 5]
print(solution(5, 5))   # 결과: [-1, 0, 1, 2, 3]