# 서로 다른 옷의 조합 수를 계산하는 함수
def solution(clothes):
    # 의상 종류별 개수를 저장할 해시맵 초기화
    hash_map = {}

    # 의상 정보를 순회하며 종류별 개수 누적
    for clothe, type in clothes:
        # 해당 종류가 이미 있으면 1 증가, 없으면 1로 초기화
        hash_map[type] = hash_map.get(type, 0) + 1

    # 의상 조합의 총 가짓수를 계산 (초기값은 곱셈을 위한 1)
    answer = 1

    # 각 종류마다 (입는 경우 수 + 입지 않는 경우 1)을 곱함
    for type in hash_map:
        answer *= (hash_map[type] + 1)

    # 아무 종류의 옷도 입지 않은 경우(공집합) 1가지를 제외
    return answer - 1

# 테스트 케이스 실행
print(solution([["crowmask", "face"], ["bluesunglasses", "face"],
                ["smoky_makeup", "face"]]))  # 5

print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"],
                ["smoky_makeup", "face"]]))  # 3
