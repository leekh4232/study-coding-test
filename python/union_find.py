# 초기 부모 노드 설정 (1~8까지 사용, index 0은 미사용)
# 각 리스트의 인덱스가 노드 번호를 나타내고, 값은 해당 노드의 부모 노드를 나타냄
parent = [i for i in range(9)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def merge(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x  # y의 루트를 x의 루트로 합침

def print_state(label):
    print(f"{label:<15} parent =", parent[1:])  # index 1~8만 출력

# 초기 상태
print_state("초기 상태")

# 1 <- 2 연결
merge(1, 2)
print_state("1 <- 2")

# 4 <- 5 연결
merge(4, 5)
print_state("4 <- 5")

# 5 <- 6 연결
merge(5, 6)
print_state("5 <- 6")

# 테스트: union 여부 확인
def is_union(x, y):
    return find(x) == find(y)

# 결과 확인
print("\n[is_union 테스트]")
print("1과 2는 같은 집합?", is_union(1, 2))  # True
print("4와 6은 같은 집합?", is_union(4, 6))  # True
print("1과 4는 같은 집합?", is_union(1, 4))  # True

# 집합 A와 B를 연결
print()             # 빈 줄 출력
merge(1, 4)
print_state("1 <- 4 (A와 B 병합)")

# 테스트: union 여부 확인
print("\n[is_union 테스트]")
print("1과 6은 같은 집합?", is_union(1, 6))  # True
print("2와 5은 같은 집합?", is_union(2, 5))  # True
print("1과 3은 같은 집합?", is_union(1, 3))  # False