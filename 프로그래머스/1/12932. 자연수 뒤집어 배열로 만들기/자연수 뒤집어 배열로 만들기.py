"""
프로그래머스 12932번 - 자연수 뒤집어 배열로 만들기

https://school.programmers.co.kr/learn/courses/30/lessons/12932
"""
def solution(n):
    # [풀이1] 특정 위치의 원소와 교환할 반대쪽 위치를 계산하는 형태
    # k = list(str(n))

    # size = len(k)
    # half = size // 2

    # for i in range(half):
    #     p = size - i - 1

    #     #k[i], k[p] = k[p], k[i]
    #     a = k[i]
    #     k[i] = k[p]
    #     k[p] = a

    # return list(map(int, k))

    # [풀이2] 문자열로 변환한 뒤, 문자열을 뒤집어서 리스트로 변환
    return list(map(int, reversed(str(n))))

if __name__ == '__main__':
    n = 12345
    print(solution(n))