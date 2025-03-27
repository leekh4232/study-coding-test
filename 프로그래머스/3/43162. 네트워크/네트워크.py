def solution(n, computers):
    # 각 컴퓨터의 방문 여부를 저장하는 리스트
    visited = [False] * n

    # 네트워크의 개수를 저장할 변수
    network_count = 0

    # 모든 컴퓨터를 하나씩 확인
    for i in range(n):
        # 아직 방문하지 않은 컴퓨터라면 새로운 네트워크 시작
        if not visited[i]:
            # DFS를 위한 스택 초기화
            stack = [i]

            # 스택이 빌 때까지 반복
            while stack:
                # 스택에서 하나 꺼냄
                current = stack.pop()

                # 아직 방문하지 않았다면 방문 처리
                if not visited[current]:
                    visited[current] = True

                    # 연결된 컴퓨터들을 스택에 추가
                    for next_computer in range(n):
                        if not visited[next_computer] and computers[current][next_computer] == 1:
                            stack.append(next_computer)

            # 하나의 네트워크 탐색이 끝났으므로 카운트 증가
            network_count += 1

    # 전체 네트워크 수 반환
    return network_count

if __name__ == "__main__":
    # 테스트 케이스 실행
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 결과: 2
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 결과: 1
