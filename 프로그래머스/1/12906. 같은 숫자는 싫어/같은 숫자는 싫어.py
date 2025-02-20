def solution(arr):
    stack = []  # 스택 역할을 하는 리스트

    for num in arr:
        if not stack or stack[-1] != num:  # 스택이 비어있거나 마지막 원소와 다르면 추가
            stack.append(num)

    return stack

# ✅ 예제 테스트 실행
if __name__ == "__main__":
    print(solution([1, 1, 3, 3, 0, 1, 1]))  # 결과: [1, 3, 0, 1]
    print(solution([4, 4, 4, 3, 3]))        # 결과: [4, 3]