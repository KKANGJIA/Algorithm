s = input() # 02984
result = 0

for i in range(len(s)):
  if int(s[i]) != 0 and result != 0: 
     result *= int(s[i])
  elif int(s[i]) == 0 or result == 0:
    result += int(s[i]) 

print(result)

# 문자열 인덱싱
# a = '02984'
# print(a[0])

# /********************************************************/

# 선생님 정답코드
# 1도 더하기가 더 유리함을 파악하지 못함

data = input() # 첫 번째 문자를 숫자로 변경하여 대입 
result = int(data[0]) 
for i in range(1, len(data)): # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행 
  num = int(data[i]) # 각각 int를 적용하지 말고 변수에 넣어서 사용하기
  if num <= 1 or result <= 1: 
    result += num 
  else: 
    result *= num 
    
print(result)






