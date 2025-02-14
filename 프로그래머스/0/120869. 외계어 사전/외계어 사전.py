def solution(spell, dic):
    # 기본적으로 단어가 존재하지 않는다고 가정하고 2로 설정
    answer = 2

    # dic에 있는 단어를 하나씩 확인
    for d in dic:
        # set을 사용하여 spell의 문자들이 단어 d에 모두 포함되어 있는지 확인
        if set(spell) == set(d):
            answer = 1  # 조건을 만족하면 1을 반환
            break  # 더 이상 확인할 필요 없으므로 반복 종료

    return answer  # 최종 결과 반환

# ✅ 예제 테스트 실행
print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
# 결과: 2 (spell의 문자 'p', 'o', 's'를 모두 포함하는 단어가 없음)

print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
# 결과: 1 (spell의 문자 'z', 'd', 'x'를 모두 포함하는 단어 "dzx"가 존재)

print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))
# 결과: 2 (spell의 문자 's', 'o', 'm', 'd'를 모두 포함하는 단어가 없음)
