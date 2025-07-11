def solution(sizes):
    # 명함 지갑의 가로 길이 후보 리스트를 저장할 변수
    w = []
    # 명함 지갑의 세로 길이 후보 리스트를 저장할 변수
    h = []

    # 모든 명함의 크기를 순회하면서
    for size in sizes:
        # 명함을 회전시켜서 가로가 항상 더 길거나 같도록 정렬
        if size[0] > size[1]:
            # size[0]이 더 크면 그대로 가로로 사용
            w.append(size[0])
            h.append(size[1])
        else:
            # size[1]이 더 크면 회전시켜서 가로로 사용
            w.append(size[1])
            h.append(size[0])

    # 가장 큰 가로 길이와 가장 큰 세로 길이를 곱하여 최소 지갑 크기 계산
    return max(w) * max(h)

# 테스트 케이스 실행
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))    # 출력 -> 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))   # 출력 -> 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))   # 출력 -> 133