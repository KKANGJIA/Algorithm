'''
# 최댓값의 인덱스 번호 구하기
n = map(int, input().split())

result = list(n)

for i in result:
    max_val = max(result)
    indexnum = result.index(max_val)

print(indexnum)
'''

# 최댓값의 인덱스 번호 구하기 함수로 구현
def find_max_idx(a):
    n = len(a) # 입력크기 n
    max_idx = 0 # 리스트 중 0번 위치를 최댓값으로 기억
    for i in range(1, n): 
        if a[i] > a[max_idx]: # i가 최댓값보다 크면
            max_idx = i # i를 최댓값에 대입하기
    return max_idx

# 알고리즘 실행
v = [17, 92, 18, 33, 58, 7 ,33, 42]
print(find_max_idx(v))
