# 니의 풀이

# n =25 k= 3

n,k = map(int, input().split())
count = 0

while n > 1:
  if n % k == 0:
    n = n // k
    count += 1
  elif  n % k != 0:
    n = n - 1
    count += 1

print(count) # 3

# /*****************************************************************************************************************/

# 선생님 풀이
# 풀이를 이렇게 작성한 이융 반복문을 한번돌때마다 한번씩 나누기를 수행하기 때문에 시간복잡도가 로그시간이 되므로 효율적이다.

n, k = map(int, input().split())
result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k # K로 나누어 떨어지는 수
    result += (n - target) # target 까지 가기위해 1빼기 진행
    n = target
    if n < k:
        break # 못 나누는 경우 break
    result += 1 # 2번 연산 (나누기) 수행 한번 했으니 +1
    n //= k 

result += (n - 1) # 1이 될 때까지 빼야하므로.
print(result)