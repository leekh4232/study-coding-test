"""
프로그래머스 12932번 - 자연수 뒤집어 배열로 만들기

https://school.programmers.co.kr/learn/courses/30/lessons/12932
"""
def solution(n):
    return list(map(int, reversed(str(n))))

if __name__ == '__main__':
    n = 12345
    print(solution(n))