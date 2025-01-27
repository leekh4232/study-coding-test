# B가 A를 한 칸씩 밀어 가능한 문자열이라면 B를 반복했을 때 A가 B안에 들어있어야 한다.
# 예를 들어, A = 'abca', B='aabc'일 때 B * 2는 'aabcaabc'이다. 
# B * 2에 A가 들어있고, 그 위치는 1번 인덱스이다.
# 이 과정이 if 문에 작성되어 있다. A가 B에 포함되어 있으면 A의 위치를 find() 함수로 찾아 리턴한다.
# find() 함수는 abca에서 첫 번째 문자열의 위치를 리턴해주므로 1이 리턴된다.
def solution(A, B):
    B *= 2
    
    if A in B:
        return B.find(A)
    else:
        return -1