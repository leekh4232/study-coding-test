def solution(my_string):
    answer = 0

    for m in my_string:
        if m.isnumeric():
            answer += int(m)

    return answer

print(solution("aAb1B2cC34oOp")) # 10
print(solution("1a2b3c4d123"))   # 16