n = int(input())

str = ""
    
for i in range(n):
    for j in range(i+1):
        str += "*"

    if i + 1 < n:
        str += "\n"

print(str)