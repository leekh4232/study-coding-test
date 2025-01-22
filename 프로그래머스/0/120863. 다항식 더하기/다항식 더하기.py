def solution(polynomial):
    vals = [0,0]

    poly = polynomial.split(" + ")
    print(poly)

    for p in poly:
        if p[0] == 'x':
            vals[0] += 1
        elif p[-1] == 'x':
            vals[0] += int(p[:-1])
        else:
            vals[1] += int(p)

    if vals[0] == 0:
        answer = str(vals[1])
        return answer
    elif vals[0] == 1:
        answer = "x"
    else:
        answer = "%dx" % vals[0]

    if vals[1] > 0:
        if answer:
            answer = "%s + %d" % (answer, vals[1])
        else:
            answer = "%d" % vals[1]

    return answer

if __name__ == "__main__":
    print(solution("1"))