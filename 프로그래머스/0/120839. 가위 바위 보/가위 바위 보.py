def solution(rsp):
    # 1. 변환 규칙을 딕셔너리로 정의 (각 숫자가 이기는 값으로 매핑)
    win_dict = {'0': '5', '2': '0', '5': '2'}

    # 2. 변환된 값을 저장할 리스트 초기화
    answer = []
    
    # 3. 각 문자를 순회하며 변환 수행
    for r in rsp:
        answer.append(win_dict[r])  # 변환된 값을 리스트에 추가

    # 4. 리스트를 문자열로 변환하여 반환
    return ''.join(answer)

# ✅ 예제 테스트 실행
print(solution("2"))     # 결과: "0"
print(solution("205"))   # 결과: "052"