def solution(my_string):
    # 1. 문자열을 소문자로 변환
    lowstr = my_string.lower()

    # 2. 소문자로 변환된 문자열을 정렬 (알파벳 순서대로 정렬됨)
    sort_str = sorted(lowstr)

    # 3. 정렬된 리스트를 문자열로 변환하여 반환
    answer = "".join(sort_str)

    return answer

# ✅ 예제 테스트 실행
print(solution("Bcad"))
# 결과: "abcd" (소문자로 변환 후 정렬)

print(solution("heLLo"))
# 결과: "ehllo" (소문자로 변환 후 정렬)

print(solution("Python"))
# 결과: "hnopty" (소문자로 변환 후 정렬)