# # 문제풀이 아이디어 잘못됨 ㅠㅠ

# # 풀이
# # 각 종류별 count를 계산
# # 계산한 count를 통해서 (count+1)를 곱해주고 마지막에 1을 빼줌
# # 각 카테고리별로 다음과 같이 “해당 카테고리의 아이템을 장착하지 않는 경우” 한개를 더 추가해서 계산해야한다.(count+1)
# # 스파이는 반드시 한 개의 아이템은 장착해야 하므로 1을 빼주는 이유는 모두 안입은 경우를 제거
# # (모자 갯수 + 1) (안경 갯수 + 1) (신발 갯수 + 1) - 1
# from operator import mul
# from functools import reduce
# from collections import Counter


# def solution(clothes):
#     answer = {}
#     for i in clothes:
#         if i[1] in answer:
#             answer[i[1]] += 1
#         else:
#             answer[i[1]] = 1

#     cnt = 1
#     for i in answer.values():
#         cnt *= (i+1)
#     return cnt - 1

from collections import Counter
from functools import reduce


def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    # ['headgear', 'eyewear', 'headgear']
    print([kind for name, kind in clothes])
    # Counter({'headgear': 2, 'eyewear': 1})
    print(Counter([kind for name, kind in clothes]))
    # reduce( 함수, 리스트 , 초기값): 리스트에 있는 원소를 중첩으로 사용하여 하나의 반환값을 만들어낸다.
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


''' reduce와 mul을 사용한 간결한 코드
from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
'''

clothes = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crowmask", "face"], [
# "bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))
