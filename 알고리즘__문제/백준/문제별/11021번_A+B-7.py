T = int(input())  # 테스트케이스개수

A = []

for i in range(T):
    A.append(input().split())

# print(A) [['1', '1'], ['2', '3'], ['3', '4'], ['9', '8'], ['5', '2']]

n = len(A)
test = []
for i in range(n):
    test.append(int(A[i][0]) + int(A[i][1]))
    print(f'Case #{i+1}: {test[i]}')
