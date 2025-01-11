"""
프로그래머스 42586번 - 기능개발
https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""
import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()

    for i in range(len(progresses)):
        d = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(d)

    cnt = 1  # 완료된 기능
    prev = days.popleft()

    while len(days) > 0:
        cur = days.popleft()
        if prev >= cur:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            prev = cur

    answer.append(cnt)
    return answer


if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))  # [2, 1]

    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(progresses, speeds))  # [1, 3, 2]
