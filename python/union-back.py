def find(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

def solution(cities, plan):
    n = len(cities)
    parents = [i for i in range(n)]

    # 연결 정보 기반으로 유니온
    for i in range(n):
        for j in range(n):
            if cities[i][j] == 1:
                union(parents, i, j)

    # 여행 계획이 모두 같은 그룹인지 확인
    root = find(parents, plan[0])
    for city in plan[1:]:
        if find(parents, city) != root:
            return "NO"
    return "YES"

# 테스트 실행
cities = [[0, 1, 0],
          [1, 0, 1],
          [0, 1, 0]]
plan = [0, 1, 2]

print(solution(cities, plan))  # 👉 YES 출력