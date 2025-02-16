def solution(array):
    # 1. 배열에서 가장 큰 값을 찾음
    max_value = max(array)
    
    # 2. 가장 큰 값의 인덱스를 찾음
    max_index = array.index(max_value)
    
    # 3. 결과를 리스트 형태로 반환
    return [max_value, max_index]

# ✅ 예제 테스트 실행
print(solution([1, 8, 3]))  # 결과: [8, 1]
print(solution([9, 10, 11, 8]))  # 결과: [11, 2]