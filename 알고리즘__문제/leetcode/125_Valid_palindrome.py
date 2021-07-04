def isPalindrome(s):
    characters = ":,"
    remove_characters = ''.join(x for x in s if x not in characters)
    remove_blank = (''.join(remove_characters.split())).lower()

    return True if remove_blank == remove_blank[::-1] else False


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))


'''
1. 리스트 풀이
def isPalindrome(self, s:str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    #팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return FaLse
    
    return True

2. 데크자료형을 이용한 최적화
def isPalindrome(self, s:str) -> bool:
    #자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    
    return True

3.슬라이싱 사용
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] # 슬라이싱, reversed() + join()보다 빠름
'''
