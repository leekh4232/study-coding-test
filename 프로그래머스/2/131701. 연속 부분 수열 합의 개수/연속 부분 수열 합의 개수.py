def solution(elements):
    res = set()                     # 결과를 저장할 집합 (중복 제거를 위해 사용)
    n = len(elements)               # 수열의 길이
    ext = elements * 2              # 원형 수열을 처리하기 위해 수열을 두 배로 확장
    
    for length in range(1, n + 1):  # 모든 길이에 대해 반복
        left, right = 0, length - 1 # 투포인터 초기화
        win_sum = sum(elements[:length]) # 초기 윈도우 합 계산
        res.add(win_sum)            # 초기 합을 결과 집합에 추가
        
        while right + 1 < n + length:
            win_sum = win_sum - ext[left] + ext[right + 1] # 윈도우 이동
            left += 1
            right += 1
            res.add(win_sum)        # 업데이트된 합을 결과 집합에 추가
    
    return len(res)                 # 중복을 제거한 연속 부분 수열 합의 개수를 반환

if __name__ == "__main__":
    print(solution([7, 9, 1, 1, 4]))  # 18