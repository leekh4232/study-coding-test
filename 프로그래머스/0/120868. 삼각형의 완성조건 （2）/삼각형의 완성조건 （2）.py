def solution(sides):
    # 가장 짧은 변의 길이
    shortest = min(sides)
    
    # 가장 긴 변의 길이
    longest = max(sides)

    # 1. 나머지 변이 가장 긴 변이 되는 경우 (x > longest - shortest)
    # 2. 기존 가장 긴 변보다 작아야 하는 경우 (x < longest + shortest)
    # 가능한 정수 개수는 2 * shortest - 1로 계산됨
    answer = 2 * shortest - 1
    
    return answer

# ✅ 예제 테스트 실행
print(solution([1, 2]))  
# 결과: 1 (가능한 변의 길이: 1)

print(solution([3, 6]))  
# 결과: 5 (가능한 변의 길이: 4, 5, 6, 7, 8)

print(solution([11, 7]))  
# 결과: 13 (가능한 변의 길이: 5부터 17까지)