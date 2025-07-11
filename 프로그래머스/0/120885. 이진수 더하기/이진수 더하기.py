def solution(bin1, bin2):
    # 이진수를 10진수로 변환
    a = int(bin1, 2)
    b = int(bin2, 2)

    # 10진수로 변환된 두 수를 더한 후, 다시 이진수로 변환
    answer = bin(a + b)

    # "0b" 접두사를 제거하고 반환
    return answer[2:]

# ✅ 예제 테스트 실행
print(solution("10", "11"))
# 결과: "101" (2 + 3 = 5 → "101")

print(solution("1001", "1111"))
# 결과: "11000" (9 + 15 = 24 → "11000")