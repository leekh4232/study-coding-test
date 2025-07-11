def solution(n: int) -> int:
    mylist = list(map(int, str(n)))
    length = len(mylist)

    for i in range(length):
        swapped = False
        for j in range(0, length-i-1):
            if mylist[j] < mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
                swapped = True

        if not swapped:
            break

    return int(''.join(map(str, mylist)))

if __name__ == '__main__':
    param = int(input())
    print(solution(param))