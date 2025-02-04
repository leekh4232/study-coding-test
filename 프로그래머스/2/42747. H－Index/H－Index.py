def solution(citations):
    answer = 0

    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] >= i + 1:
            answer = i + 1
        else:
            break

    return answer

if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    # 3
    print(solution(citations))