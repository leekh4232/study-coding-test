# from itertools import permutations

# 숫자가 소수인지 판별하는 함수를 정의한다.
def isPrime(num):
    # 1 이하의 숫자는 소수가 아니다.
    if num <= 1:
        return False
    # 2부터 숫자의 제곱근까지 반복하며 나누어 떨어지는지 확인한다.
    for i in range(2, int(num**0.5) + 1):
        # 나누어 떨어진다면 소수가 아니다.
        if num % i == 0:
            return False
    # 위 조건에 해당하지 않으면 소수이다.
    return True

# 주어진 숫자 조각들로 만들 수 있는 소수의 개수를 찾는 함수를 정의한다.
def solution(numbers):
    # 소수의 개수를 저장할 변수를 0으로 초기화한다.
    answer = 0
    # 찾은 소수들을 저장할 중복 없는 집합(set)을 생성한다.
    result = set()

    # 백트래킹을 수행하는 중첩 함수를 정의한다.
    # currentNum: 현재까지 만들어진 숫자를 문자열 형태로 저장한다.
    # visited: 이미 사용된 numbers의 인덱스를 저장하는 집합이다.
    def backtrack(currentNum, visited):
        # currentNum이 비어있지 않다면 (즉, 숫자가 생성되었다면)
        if currentNum:
            # currentNum을 정수로 변환하여 소수인지 확인한다.
            if isPrime(int(currentNum)):
                # 소수라면 result 집합에 추가한다.
                result.add(int(currentNum))

        # numbers의 각 숫자 조각에 대해 반복한다.
        for i in range(len(numbers)):
            # 현재 인덱스 i의 숫자 조각이 아직 사용되지 않았다면
            if i not in visited:
                # visited 집합을 복사하여 새로운 visited 집합을 만든다.
                newVisited = set(visited)
                # 새로운 visited 집합에 현재 인덱스 i를 추가한다.
                newVisited.add(i)
                # 현재 숫자(currentNum)에 numbers[i]를 추가하여 재귀 호출한다.
                backtrack(currentNum + numbers[i], newVisited)

    # 초기 호출: 빈 문자열과 빈 집합으로 백트래킹을 시작한다.
    backtrack("", set())

    # result 집합에 있는 소수들의 개수를 반환한다.
    return len(result)

# 직접 테스트를 위한 코드 블록이다.
if __name__ == "__main__":
    # "17"로 만들 수 있는 소수의 개수를 출력한다. (예상 출력: 3)
    print(solution("17"))
    # "011"로 만들 수 있는 소수의 개수를 출력한다. (예상 출력: 2)
    print(solution("011"))