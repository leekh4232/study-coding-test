def solution(a, b, g, s, w, t):
    # 초기 정답은 무한대로 설정
    answer = float('inf')

    start = 0
    end = 4 * 10**14  # 최대 시간 예상치

    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0

        for i in range(len(g)):
            # mid 시간 동안 이동 가능한 횟수 계산
            moves = mid // (t[i] * 2)
            if mid % (t[i] * 2) >= t[i]:
                moves += 1

            maxCarry = moves * w[i]
            gold += min(g[i], maxCarry)
            silver += min(s[i], maxCarry)
            total += min(g[i] + s[i], maxCarry)

        # 조건 만족 시 정답 후보 업데이트, 시간 줄이기
        if gold >= a and silver >= b and total >= a + b:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1

    return answer

# 테스트 예제
print(solution(10, 10, [100], [100], [7], [10]))  # -> 50
print(solution(90, 500, [70,70,0], [0,0,500], [100,100,2], [4,8,1]))  # -> 499