# 문자열안에 다른 문자열이 들어있는지 아닌지 if ~ in으로 확인이 가능!!!
# 접두어라는 조건에 맞지않아서 테스트케이스가 틀림!!!

def solution(phone_book):
    sortPB = sorted(phone_book)
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            # for 접두어 슬라이싱
            if sortPB[i] in sortPB[j][:len(phone_book[i])]:
                return False
            else:
                continue
    return True


# 8,9는 정렬위한, 1번 접두어 15는 길이 짧은게 앞으로 오도록
# phone_book = ["113", "44", "4544"]  # 접두어 확인용 테스트케이스
phone_book = ["22222", "3333", "111111111"]  # 길이가 짧은 요소대로 정렬 테스트케이스
# phone_book = ["010111", "010"]  # 8,9번 테스트케이스 정렬필요
# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123", "456", "789"]
# phone_book = ["113333", "115555", "345555", "555555", "345444"]
# phone_book = ["12", "123", "1235", "567", "88"]
print(solution(phone_book))

# TC: 14, 15 실패
# 정확성: 75.0
# 효율성: 8.3
# 합계: 83.3 / 100.0
