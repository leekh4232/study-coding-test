def dfs(numbers, target, current, idx):
    if idx == len(numbers):
        return 1 if current == target else 0

    count = 0
    count += dfs(numbers, target, current + numbers[idx], idx + 1)
    count += dfs(numbers, target, current - numbers[idx], idx + 1)
    return count

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3)) # 5
    print(solution([4, 1, 2, 1], 4))    # 2