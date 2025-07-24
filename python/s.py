def solution(nodes, target):
    # 입력으로 받은 nodes 리스트를 직접 수정하기 위해 복사
    arr = list(nodes)
    n = len(arr)

    # DFS 함수 정의: 특정 노드와 그 자손들을 '제거' 표시(-2)
    def dfs(num, current_arr):
        current_arr[num] = -2  # 현재 노드를 제거된 것으로 표시
        for i in range(len(current_arr)):
            # 현재 노드가 i번 노드의 부모라면 (즉, i번 노드가 현재 노드의 자식이라면)
            if num == current_arr[i]:
                # 자식 노드에 대해 재귀적으로 dfs 호출
                dfs(i, current_arr)

    # 제거할 대상 노드(target)부터 DFS를 시작하여 모든 관련 노드를 제거 표시
    dfs(target, arr)

    count = 0
    for i in range(n):
        # 제거되지 않은 노드(-2가 아님)이면서
        # 그 노드가 다른 어떤 노드의 부모도 아닌 경우 (리프 노드인 경우)
        if arr[i] != -2 and i not in arr:
            count += 1

    return count

if __name__ == "__main__":
    print(solution([-1, 0, 0, 1, 1], 2))
    print(solution([-1, 0, 0, 1, 1], 1))
    print(solution([-1, 0, 0, 1, 1], 0))
    print(solution([-1, 0, 0, 2, 2, 4, 4, 6, 6], 4))