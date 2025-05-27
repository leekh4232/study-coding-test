# solution 함수는 입력받은 number 배열에서
# 3개의 수를 선택해 합이 0이 되는 조합의 수를 찾는 함수
def solution(number):
    # 방문 여부를 저장하는 리스트를 생성 (각 인덱스별로 False로 초기화)
    visited = [False] * len(number)
    # 정답의 개수를 리스트로 관리 (참조를 통해 내부 함수에서 값 변경 가능)
    answer = [0]

    # 백트래킹 탐색을 시작 (시작 인덱스 0, 선택된 개수 0, 합계 0)
    backtracking(0, 0, 0, number, visited, answer)
    # 모든 탐색이 끝난 후, answer[0]에 저장된 정답 개수를 반환
    return answer[0]

# backtracking 함수는 현재 인덱스, 선택 개수, 누적 합, 원본 배열, 방문여부, 정답 리스트를 인자로 받음
def backtracking(index, depth, total, number, visited, answer):
    # 만약 3개를 선택했다면
    if depth == 3:
        # 선택한 3개 원소의 합이 0이면 answer[0] 증가
        if total == 0:
            answer[0] += 1
        # 3개를 다 골랐으므로 더 이상 진행하지 않고 함수 종료
        return

    # index부터 배열 끝까지 반복
    for i in range(index, len(number)):
        # 아직 방문하지 않은 인덱스라면
        if not visited[i]:
            # 해당 인덱스를 선택(방문)했다고 표시
            visited[i] = True
            # 다음 단계로 재귀 호출 (i+1부터 시작, 선택 개수+1, 합에 현재 값 더함)
            backtracking(i + 1, depth + 1, total + number[i], number, visited, answer)
            # 백트래킹: 재귀가 끝나면 선택 해제(원상 복구)
            visited[i] = False

# 예시 테스트 케이스 실행
print(solution([-2, 3, 0, 2, -5]))        # 출력: 2
print(solution([-3, -2, -1, 0, 1, 2, 3])) # 출력: 5
print(solution([-1, 1, -1, 1]))           # 출력: 0