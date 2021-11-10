T = int(input()) # 테케 개수
array_parenthesis = [] # 괄호 리스트
array_result = []
result = '' # 결과

# 양 괄호의 개수가 일치하면 Yes, 아니면 No
for _ in range(T): # 테케 입력
  array_parenthesis.append(input())
  left_cnt = 0
  right_cnt = 0
  for i in array_parenthesis:
    for j in array_parenthesis[i]:
      if '(' ==  j:
        left_cnt += 1
      elif ')' ==  j:
        right_cnt += 1
    if left_cnt == right_cnt:
      result = 'Yes'
      array_result.append(result)
    else: 
      result = 'No'
      array_result.append(result)
  
print(array_result)

  

