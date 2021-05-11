import collections


def solution(clothes):
    for i in range(1, len(clothes)):
        new_clothes = list(collections.Counter(clothes[0])).extend(
            list(collections.Counter(clothes[i])))

    #     print(list(collections.Counter(clothes[i])))
    # print(set(list(dict(clothes).values())))


clothes = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))
