def solution(my_string):
    answer = 0

    n = len(my_string)
    i = 0

    while i < n:
        tmp = ""

        while i < n:
            if my_string[i].isnumeric():
                tmp += my_string[i]
                i += 1
            else:
                break

        if tmp:
            answer += int(tmp)

        i += 1

    return answer

if __name__ == "__main__":
    print(solution("aAb1B2cC34oOp"))
    print(solution("1a2b3c4d123Z"))