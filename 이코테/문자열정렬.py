S = input() # K1KA5CB7

digit = 0
alpha = ''

for i in S:
  if i.isdigit():
    digit += int(i) 
    print(i)
  if i.isalpha():
    alpha += i
    print(i)

print(''.join(sorted(alpha)) + str(digit))

# sorted(alpha) 리스트를 반환한다
# isdigit()과 isalpha()로 알파벳인지 숫자인지 판단한다
# str은 str과만 연산이 가능하다