def solution(chicken):
    answer = 0  # 받을 수 있는 총 서비스 치킨 수를 저장할 변수
    
    while chicken >= 10:  # 쿠폰이 10장 이상일 때만 교환 가능
        div = chicken // 10  # 10개당 서비스 치킨 수 계산
        mod = chicken % 10   # 교환 후 남은 쿠폰 수 계산
        answer += div        # 총 서비스 치킨 수에 추가
        chicken = div + mod  # 새로운 쿠폰 개수로 업데이트
    
    return answer

# 테스트 예제 실행
print(solution(100))        # 11
print(solution(1081))       # 120