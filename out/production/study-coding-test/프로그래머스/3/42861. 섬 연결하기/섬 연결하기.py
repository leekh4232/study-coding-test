def solution(n, costs):
    # 다리 정보를 비용 기준으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    # 각 섬을 독립적인 집합으로 초기화 (부모 노드)
    bridges = [i for i in range(n)]

    # 각 섬별로 연결된 섬 목록을 관리하는 리스트
    room = [[i] for i in range(n)]

    # 총 건설 비용을 저장할 변수
    answer = 0
    # 만들어진 다리의 수를 저장할 변수
    made = 0

    # 정렬된 다리 리스트를 순회
    for x, y, cost in costs:
        x = bridges[x]  # 섬 x가 속한 집합 번호
        y = bridges[y]  # 섬 y가 속한 집합 번호

        # 이미 같은 집합에 속해 있으면 스킵 (사이클 발생 방지)
        if x == y:
            continue

        # 섬 y가 속한 모든 섬을 섬 x의 집합으로 합치기
        while room[y]:
            k = room[y].pop()
            room[x].append(k)

            # 부모 노드를 x로 업데이트
            bridges[k] = x

        # 다리를 선택하고 비용을 누적
        answer += cost
        made += 1

        # n-1개의 다리가 연결되면 모든 섬이 연결 완료
        if made == n - 1:
            break

    # 총 최소 비용 반환
    return answer

# 테스트 케이스 실행
if __name__ == "__main__":
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))  # 결과: 4