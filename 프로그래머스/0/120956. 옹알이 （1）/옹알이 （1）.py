def solution(babbling):
    # 발음할 수 있는 단어 리스트
    words = ["aya", "ye", "woo", "ma"]
    answer = 0

    # 각 단어에 대해 검사
    for word in babbling:
        for w in words:
            word = word.replace(w, " ")  # 발음 가능한 단어를 공백으로 변환
        if word.strip() == "":  # 모든 발음을 제거한 후 빈 문자열이면 발음 가능
            answer += 1

    return answer

# ✅ 예제 테스트 실행
print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
# 결과: 1 (발음 가능한 단어: "aya")

print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
# 결과: 3 (발음 가능한 단어: "ayaye", "ye", "yemawoo")