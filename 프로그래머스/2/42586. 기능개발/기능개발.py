from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)  # 작업 진행도를 큐로 변환
    speeds = deque(speeds)  # 작업 속도를 큐로 변환

    answer = []
    days = 0  # 경과 일수
    cnt = 0  # 배포될 기능 개수

    while progresses:  # 큐가 빌 때까지 반복
        # 첫 번째 작업이 완료되었는지 확인 (소수점 올림)
        if (progresses[0] + days * speeds[0]) >= 100:
            progresses.popleft()  # 완료된 작업 제거
            speeds.popleft()  # 해당 작업의 속도도 제거
            cnt += 1  # 배포될 기능 개수 증가
        else:
            if cnt > 0:  # 배포할 기능이 있는 경우
                answer.append(cnt)  # 배포 개수 저장
                cnt = 0  # 배포 개수 초기화
            days += 1  # 하루 증가

    answer.append(cnt)  # 마지막 배포 개수 추가
    return answer

# 테스트 예제 실행
print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]