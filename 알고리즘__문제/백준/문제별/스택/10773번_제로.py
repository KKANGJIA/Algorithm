K = int(input()) # 정수 개수
account_book = []

for i in range(K): # 정수를 한줄씩 입력
  money = int(input())
  if money != 0:
    account_book.append(money) # 0이 아니면 리스트에 추가
  else :
    account_book.pop() # 0이면 리스트의 한개의 요소를 삭제
    
print(account_book)
  
