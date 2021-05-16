# import math
# print(dir(math))
# def solution(n, m):
#     return [math.gcd(n, m), math.lcm(n, m)]

def solution(n, m):
    gcd = 1
    lcm = 1
    for i in range(1, min(n, m)+1):
        if n % i == 0 and m % i == 0:
            gcd *= i

        else:
            break
            lcm *= gcd * (n % i) * (m % i)
    print(gcd, lcm)


'''
1.
def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]

2.
def solution(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]
    return answer


    첫번째 코드는 lambda를 사용하여 m이 0일 때 m을, 0이 아니면 나머지를 다시 한번 반복시켜서 최대공약수를 구했고, 최소공배수 또한 lambda로 두수를 곱한 값에서 최대공약수를 나눠서 간결하게 구하였다. 두번째 방법에서는 max와 min으로 어느 수가 더 큰지를 판별하고 나서 두 수가 나누어 떨어질 때까지 반복해서 나누어 최대공약수를 구했다. 그리고 최소공배수는 같은 방식으로 구하였다. 
'''
n = 3
m = 12
print(solution(n, m))
