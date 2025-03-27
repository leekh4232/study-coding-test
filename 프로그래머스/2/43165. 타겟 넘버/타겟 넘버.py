def solution(numbers, target):
    stack = [(0, 0)]  # (현재 합, 인덱스)
    count = 0

    while stack:
        current, idx = stack.pop()

        if idx == len(numbers):
            if current == target:
                count += 1
        else:
            stack.append((current + numbers[idx], idx + 1))
            stack.append((current - numbers[idx], idx + 1))

    return count

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3)) # 5
    print(solution([4, 1, 2, 1], 4))    # 2
