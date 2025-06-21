# 백트래킹 함수: 현재 상태에서 이동 가능한 노드를 모두 탐색하며 최대 양을 모은다
def backtracking(info, edges, visited, sheep, wolf, answer):
    # 양이 늑대보다 많을 경우에만 유효한 상태이므로 탐색 계속
    if sheep > wolf:
        # 현재 양의 수를 결과 리스트에 저장
        answer.append(sheep)
    else:
        # 늑대가 같거나 많아지는 순간 모든 양이 잡히므로 중단
        return

    # 간선 정보를 순회하면서 현재 방문한 노드와 연결된 자식 노드를 탐색
    for parent, child in edges:
        # 부모 노드는 방문했고 자식 노드는 방문하지 않은 경우만 탐색
        if visited[parent] and not visited[child]:
            # 자식 노드를 방문 처리
            visited[child] = 1

            # 자식 노드가 양일 경우 양 수 증가
            if info[child] == 0:
                backtracking(info, edges, visited, sheep + 1, wolf, answer)
            # 자식 노드가 늑대일 경우 늑대 수 증가
            else:
                backtracking(info, edges, visited, sheep, wolf + 1, answer)

            # 백트래킹 시 자식 노드 방문 여부 원복
            visited[child] = 0

# 문제 해결 메인 함수
def solution(info, edges):
    # 각 노드 방문 여부를 저장하는 배열
    visited = [0] * len(info)
    # 가능한 결과(양 수)를 저장할 리스트
    answer = []

    # 루트 노드(0번)는 항상 양이며, 처음 방문 처리
    visited[0] = 1
    # 백트래킹 시작: 루트 노드 기준, 양 1마리, 늑대 0마리
    backtracking(info, edges, visited, sheep=1, wolf=0, answer=answer)

    # 탐색 중 저장된 결과 중 가장 큰 양 수를 반환
    return max(answer)

# 테스트 케이스 실행
print(solution(
    [0,0,1,1,1,0,1,0,1,0,1,1],
    [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],
     [4,3],[6,5],[4,6],[8,9]]
))
# 출력: 5

print(solution(
    [0,1,0,1,1,0,1,0,0,1,0],
    [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],
     [3,7],[4,8],[6,9],[9,10]]
))
# 출력: 5
