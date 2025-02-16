def solution(rsp):
    # 변환 규칙을 딕셔너리로 정의
    win_dict = {'0': '5', '2': '0', '5': '2'}
    
    # 리스트 컴프리헨션을 사용하여 변환된 값을 저장 (성능 최적화)
    answer = [win_dict[r] for r in rsp]
    
    # 리스트를 문자열로 변환하여 반환
    return ''.join(answer)

# 테스트 실행
print(solution("2"))     # 출력: "0"
print(solution("205"))   # 출력: "052"
