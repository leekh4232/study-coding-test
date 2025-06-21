def solution(sides):
    # 순서대로 정렬한다.
    # --> 2번째 원소가 가장 긴 변의 길이가 된다.
    sides.sort()
    
    # 가장 긴 변의 길이가 나머지 두 변의 길이의 합보다 작다면 삼각형 성립
    if sides[2] < sides[0] + sides[1]:
        return 1
    else:
        return 2
    
print(solution([1, 2, 3]))      # 2
print(solution([3, 6, 2]))      # 2
print(solution([199, 72, 222])) # 1