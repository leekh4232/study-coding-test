def solution(numbers):
    answer = ''

    #  문자열 비교를 통해 숫자들을 정렬해야 하므로 문자열로 변환
    numbers = list(map(str, numbers))

    # 3의 배수로 만들어서 비교
    # 숫자 3과 30을 비교할 때, 3을 세 번 반복하면 333, 30을 세 번 반복하면 303030이 됨.
    # 이 두 문자열을 비교하면 333이 더 크기 때문에 3이 30보다 앞에 오게 된다.
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(numbers)))

    return answer

if __name__ == '__main__':
    numbers = [6, 10, 2]
    # 6210
    print(solution(numbers))

    numbers = [3, 30, 34, 5, 9]
    # 9534330
    print(solution(numbers))