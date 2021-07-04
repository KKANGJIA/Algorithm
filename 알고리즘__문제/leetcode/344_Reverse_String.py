def reverseString(self, s: List[str]) -> None:
    s.reverse()  # s = s[::-1]와 동일


'''
# 책 , 위의 방법으로 푸는 게 더빠르게 진행 가능
1. 투포인트 스왑 방법
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s)-1

    while left < right:
        s[left], s[right] = s[left], s[right]
        left += 1
        right -= 1

'''
