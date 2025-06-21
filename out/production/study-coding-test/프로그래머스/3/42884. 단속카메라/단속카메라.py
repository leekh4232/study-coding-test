def solution(routes):
    # 최소 설치해야 하는 카메라 수, 첫 번째 카메라는 무조건 설치
    answer = 1

    # 차량들의 이동 경로를 진출 지점 기준으로 오름차순 정렬
    routes.sort(key=lambda x: x[1])

    # 첫 번째 차량의 진출 지점에 카메라 설치
    camera = routes[0][1]

    # 나머지 차량들을 순서대로 확인
    for route in routes[1:]:
        # 현재 차량의 진입 지점이 기존 카메라 위치보다 크다면
        if camera < route[0]:
            # 새로운 카메라를 현재 차량의 진출 지점에 설치
            camera = route[1]
            answer += 1  # 카메라 설치 개수 증가

    # 총 설치한 카메라 수 반환
    return answer

# 테스트 케이스 실행
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 결과: 2