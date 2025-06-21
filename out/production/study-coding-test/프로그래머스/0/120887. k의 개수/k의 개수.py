def solution(i, j, k):
    answer = 0  # 결과를 저장할 변수 초기화
    k = str(k)  # k를 문자열로 변환

    for n in range(i, j+1):  # i부터 j까지 반복
        answer += str(n).count(k)  # n을 문자열로 변환하여 k의 개수를 카운트하여 누적

    return answer  # 최종 등장 횟수 반환

# 테스트 예제 실행
print(solution(1, 13, 1))   # 6
print(solution(10, 50, 5))  # 5
print(solution(3, 10, 2))   # 0