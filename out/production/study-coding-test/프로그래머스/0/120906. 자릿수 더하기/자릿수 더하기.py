def solution(n):
    # 1. 각 자리 숫자를 저장할 리스트 초기화
    mylist = []

    # 2. `n`을 문자열로 변환하고, 각 문자를 정수로 변환하여 리스트에 추가
    for s in str(n):
        mylist.append(int(s))

    # 3. 리스트 내 숫자의 합을 계산
    answer = sum(mylist)

    # 4. 최종 결과 반환
    return answer

# ✅ 예제 테스트 실행
print(solution(1234))   # 결과: 10
print(solution(930211)) # 결과: 16