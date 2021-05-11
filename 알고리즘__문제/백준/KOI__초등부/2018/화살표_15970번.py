# 문제해석 잘못 접근... 풀이전략부터 다시짜기
# 입력값 리스트 내포한 거 반복학습하기

import sys

N = int(input())  # 점들의 개수

point_arr = []  # 입력을 저장할 리스트
for _ in range(N):
    # 리스트 컴프리헨션을 이용 ★★입력 패턴 기억하기★★
    point_arr.append([int(i) for i in sys.stdin.readline().split()])
# print(point_arr)

# 리스트 ★안과 밖★에서 정렬
# print(sorted(point_arr))
points = sorted(point_arr)  # 점들을 리스트로 정렬

arrow_length1 = []
arrow_length2 = []
for i in range(0, N-2):  # 0~N-1
    if points[i][1] == points[i+1][1]:  # 색깔이 같은 것 중에
        # print(points[i][1], points[i+1][1])
        arrow_length1.append(points[i+1][0] - points[i][0])  # 큰 값 - 작은 값
# print(arrow_length1)
# if points[N-1][1] == points[N-2][1]:
# print(points[N-1][0], points[N-2][0])
# arrow_length2.append(points[N][0] - points[N-1][0])


# 풀이참고 1
def fcn(arr):
    sum = 0
    for i in range(len(arr)):
        if i == 0:
            sum += arr[1] - arr[0]
        elif i == len(arr) - 1:
            sum += arr[len(arr) - 1] - arr[len(arr) - 2]
        else:
            if arr[i + 1] - arr[i] >= arr[i] - arr[i - 1]:
                sum += arr[i] - arr[i - 1]
            else:
                sum += arr[i + 1] - arr[i]

    return sum


ans = 0
n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([b, a])

arr.sort()
l = arr[-1][0]

for i in range(1, l+1):
    x = []
    for j in range(n):
        if arr[j][0] == i:
            x.append(arr[j][1])
    ans += fcn(x)
print(ans)

# 풀이참고 2
# 우선 입력을 정렬한다. 겹치는게 없으므로 정렬 조건은 설정 안해도 된다.
# 입력받은 좌표를 하나하나 돌아가면서
# 현재 좌표보다 왼쪽에 있는 것중에 색이 같은것을 찾는다.
# 현재 좌표보다 오른쪽에 있는 것중에 색이 같은것을 찾는다.
# tmpret에 왼쪽, 오른쪽 값이 나오는데 그 중에서 작은것을 골라 답에 더해준다

n = int(sys.stdin.readline())

d = []
for _ in range(n):
    d.append([int(i) for i in sys.stdin.readline().split()])  # 2차원 배열로 입력받기

d.sort()  # 2차원 리스트 정렬
ret = 0

for i in range(n):  # n개 만큼 반복문 돌고
    tmploc, tmpclr = d[i]  # 임시위치와 임시색상에 2차원 리스트의 요소를 저장
    tmp = i-1
    tmpret = [9912341234, 9912341234]
    # left
    while tmp >= 0:  # 임시가 0보다 크거나 같을 때 무한 반복
        if d[tmp][1] == tmpclr:  # 색상이 같으면
            tmpret[0] = abs(tmploc - d[tmp][0])
            break
        else:
            tmp -= 1

    # right

    tmp = i+1
    while tmp < n:
        if d[tmp][1] == tmpclr:
            tmpret[1] = abs(tmploc - d[tmp][0])
            break
        else:
            tmp += 1
    ret += min(tmpret)


print(ret)


# 풀이참고3
# 같은 색깔을 가진 원소들의 화살표 총길이를 계산하는 함수
def distance(a):
    leng = 0
    for i in range(len(a)):
        if i == 0:  # 맨앞
            leng += abs(a[i] - a[i + 1])
        elif i == len(a) - 1:  # 맨뒤
            leng += abs(a[i] - a[i - 1])
        else:
            # i + 1 과 i - 1 까지의 차이를 비교해서 작은 친구를 채택
            leng += min(abs(a[i] - a[i - 1]), abs(a[i] - a[i + 1]))
    return leng


# main
n = int(input())  # 점의 갯수
answer = 0  # 출력값 변수
arr_swp = []  # 점의 정보를 담을 리스트

for i in range(n):
    loc, clr = map(int, input().split())
    arr_swp.append([clr, loc])  # [[1, 0], [2, 1], [1, 3], [2, 4], [1, 5]]
arr_swp.sort()  # [[1, 0], [1, 3], [1, 5], [2, 1], [2, 4]]
# d


# 색의 갯수
num_clr = arr_swp[-1][0]
for i in range(1, num_clr+1):  # 색의 갯수는 1부터 존재
		same_clr = []  # 같은 색인 점들의 위치정보를 모으는 리스트
    for j in range(n): #원소의 갯수 만큼 반복
        if arr_swp[j][0] == i:
            same_clr.append(arr_swp[j][1])
    answer += distance(same_clr)

print(answer)
