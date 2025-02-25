def solution(my_string):
    answer = list(my_string)  # 문자열을 리스트로 변환하여 answer에 저장
    n = len(answer)  # 문자열의 길이를 n에 저장

    for i in range(n // 2):  # 문자열의 절반 길이만큼 반복
        p = n - i - 1  # 뒤에서부터의 인덱스를 계산
        answer[i], answer[p] = answer[p], answer[i]  # 앞뒤 문자를 교환

    return "".join(answer)  # 리스트를 다시 문자열로 변환하여 반환

# 테스트 예제 실행
print(solution("jaron"))  # "noraj"
print(solution("bread"))  # "daerb"