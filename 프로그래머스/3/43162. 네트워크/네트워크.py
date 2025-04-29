# 주어진 컴퓨터들 간의 연결 정보를 이용해 네트워크의 개수를 찾는 함수
def solution(n, computers):
    # 각 컴퓨터의 방문 여부를 저장하는 리스트 초기화
    visited = [False] * n

    # 네트워크의 개수를 저장할 변수
    networkCount = 0

    # 모든 컴퓨터를 하나씩 확인
    for i in range(n):
        # 아직 방문하지 않은 컴퓨터라면 새로운 네트워크 탐색 시작
        if not visited[i]:
            # DFS 탐색을 위한 스택 초기화
            stack = [i]

            # 스택이 빌 때까지 반복
            while stack:
                # 스택에서 하나 꺼내 현재 컴퓨터를 얻음
                current = stack.pop()

                # 현재 컴퓨터가 아직 방문되지 않았다면
                if not visited[current]:
                    # 방문 처리
                    visited[current] = True

                    # 현재 컴퓨터와 연결된 다른 컴퓨터들을 스택에 추가
                    for nextComputer in range(n):
                        if not visited[nextComputer] and computers[current][nextComputer] == 1:
                            stack.append(nextComputer)

            # 하나의 네트워크 탐색이 끝났으므로 네트워크 수를 1 증가
            networkCount += 1

    # 전체 네트워크 수 반환
    return networkCount

# 메인 코드: 테스트 케이스 실행
if __name__ == "__main__":
    # 첫 번째 테스트 케이스 실행 (결과: 2)
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    # 두 번째 테스트 케이스 실행 (결과: 1)
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
