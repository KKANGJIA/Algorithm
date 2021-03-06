# input()  키보드로 문자열을 입력받아 반환(그래서 int로 변환하는 이유)

# If, while의 복합문일때 :앞을 헤더, :뒤를 스위트(suite) 즉, 실행문이라고 함

# """ """ -> docstring

# 복합문에서 스위트가 단순문이면 헤더와 스위트를 한줄에 작성가능
# 복합문 헤더 뒤에 복합문 사용 불가

# 클래스명은 카멜케이스(CamelCase), 함수명은 스네이크(snake_case)형식 권장

# 결정트리구조: 네모 안의 조건이 성립하면 검은색, 아니면 파란색 선을 따라 왼쪽에서 오른쪽으로 나아가는 나무모양으로 조합을 나열한 것

# 단항연산자 -a
# 이항연산자 a > c
# 삼항연산자 a if b else c

# 비교연산자를 연속으로 사용하는 방법과 드모르간 법칙
# 1. 비교연산자 연속으로 사용하는 방법
# if no <= 10 <= 99:
# 반복문을 종료하기위한 조건
# 2. 드모르간 법칙
# if not(no < 10 or no > 99):
# 반복문을 계속하기위한 조건
# x and y == not(not x or not y)
# x or y == not(not x and not y)

# 구조적 프로그래밍: 입력과 출력으로 이루어진 구성요소를 계층적으로 배치하여 프로그램을 구성하는 방법
# 순차, 선택, 반복 세종류의 제어흐름 사용

# 다중루프문: 반복문 안에 반복문이 들어오는 경우
# 반복문이 중첩하는 개수에 따라 이중루프 삼중루프라고 부르고 이것들을 다중루프라고 한다.
'''
for i in range(1, 10):  # 행을 나타내는 루프(세로)
    for j in range(1, 10):  # 열을 나타내는 루프(가로)
        print()
'''
#  난수 생성하기: random.randint(A, B): A이상 B이하 난수를 무작위로 1개뽑는 함수
'''
n = int(input())

for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()
# 4
# *
# **
# ***
# ****
'''

N = int(input())

for i in range(N):
    for _ in range(N-i-1):
        print(' ', end='')
    for _ in range(i+1):
        print('*', end='')

    print()
# 공백과 숫자를 같은 종속으로 들여쓰기를 해야함!!!
# 5
#     *
#    **
#   ***
#  ****
# *****
