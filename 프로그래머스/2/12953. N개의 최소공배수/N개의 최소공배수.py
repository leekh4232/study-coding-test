import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return lcm(arr[0], solution(arr[1:]))