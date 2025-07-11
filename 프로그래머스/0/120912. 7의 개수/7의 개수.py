def solution(array):
    return str(array).count("7")  # 리스트 전체를 문자열로 변환 후 "7"의 개수 카운트

# 테스트 예제 실행
print(solution([7, 77, 17]))    # 4
print(solution([10, 29]))       # 0