
def solution(n):
    cnt = 0
    for n in range(2, n+1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            cnt += 1
    return cnt
# for문이 종료된 시점에서 종료가 모긍 반복을 다 수행한 후의 종료인지
# 아니면 break에 의한 강제종료인지 구분해줄 for~ else문
# for문이 마지막까지 반복하고 끝내면 else가 실행,
# break를 만나면 else는 수행하지않고 for문을 빠져나간다


'''#  에라토스테네스의 체: 대량의 소수를 판별하고자 할 때 사용
def solution(n):
    num=set(range(2,n+1)) # 2부터 n+1까지의 집합

    for i in range(2,n+1): # 2부터 n까지 반복문
        if i in num: # 만약 i가 num 집합에 있다면
            num-=set(range(2*i,n+1,i)) # i의 배수는 num 집합에서 제외
    return len(num) # num에 남아있는 숫자의 개수가 소수의 개수
'''


n = 10
print(solution(n))
