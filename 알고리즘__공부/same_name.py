# 동명이인 찾기

def find_same_name(a):
    n = len(a)
    same_name = []
    for i in range(0, n-1):  # 개수가 인덱스 크기보다 +1이니까 n-1개라고 지정해줘야함
        for j in range(i+1, n):
            if a[i] == a[j]:
                same_name.append(a[i])
    return same_name


name = ['tom', 'jerry', 'mike', 'tom']
print(find_same_name(name))
# 시간복잡도는 n(n-1) / 2 로 O(n^2)이다

# 연습문제 1

# n명에서 두 명을 뽑아 짝으로 만드는 모든 경우를 찾는 알고리즘
# 입력: n명의 이름이 들어 있는 리스트
# 출력: 두 명을 뽑아 만들 수 있는 모든 짝


def print_pairs(a):
    n = len(a)                     # 리스트의 자료 개수를 n에 저장
    for i in range(0, n - 1):      # 0부터 n - 2까지 반복
        for j in range(i + 1, n):  # i + 1부터 n - 1까지 반복
            print(a[i], "-", a[j])


name = ["Tom", "Jerry", "Mike"]
print_pairs(name)
print()  # 한 줄 띄우기
name2 = ["Tom", "Jerry", "Mike", "John"]
print_pairs(name2)


# 연습문제 2 대문자 표기법으로 작성
# A 65536 = > O(1)
# B n - 1 = > O(n)
# C 2n ^ 2 + 10000m = > O(n ^ 2)
# D 3n ^ 2 - 4n ^ 2 + 5n ^ 2 - 6n + 7 = > O(n ^ 4)
