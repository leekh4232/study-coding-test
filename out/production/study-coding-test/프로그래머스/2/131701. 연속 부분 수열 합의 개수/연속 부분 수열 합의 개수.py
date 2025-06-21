def solution(elements):
    res = set()
    n = len(elements)
    ext = elements * 2  # 원형 수열을 위해 확장

    for size in range(1, n + 1):  # 부분 수열의 길이
        win_sum = sum(elements[:size])  # 초기 윈도우 합 계산
        res.add(win_sum)

        for i in range(1, n):  # 슬라이딩 윈도우 적용
            win_sum = win_sum - ext[i - 1] + ext[i + size - 1]
            res.add(win_sum)

    return len(res)

if __name__ == "__main__":
    print(solution([7, 9, 1, 1, 4]))  # 18