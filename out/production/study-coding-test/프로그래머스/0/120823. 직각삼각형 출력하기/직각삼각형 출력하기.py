n = int(input())

for i in range(n):
    star = ""
    for j in range(0, i+1):
        star += "*"
    print(star)