# 첫째줄에는 떡의 개수N과 요청한 길이인 M이 주어진다
# 둘째 줄에는 개별의 떡의 길이가 주어진다. 떡 높이의 총합은 할상 M이상이므로
# 손님은 필요한 양만큼 떡을 사갈 수 있다. 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

# 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
n,m = list(map(int, input().split())) # 떡의 개수와 요청한 떡 길이
rice = sorted(map(int, input().split())) # 떡의 길이 입렵, 정렬

total = 0 # 떡볶이 길이 총 합
mid = 1 # 중간 인덱스 정하기

def findHeight(array, num, length, mid):
  if mid == 0: # 전체 경우를 다 고려해봐야 하므로
    return sum(array) - (array[mid] * array)
    
  for i in range(mid, num): # mid부터 다음 인덱스들만 높이보다 커서 잘리니까 
    global total # 함수 내에서 지역변수만 인식하므로 전역변수에서 불러오기(지역변수 미할당이라는 오류방지위해)
    total += array[i] - array[mid] # 잘린 총합 구하기
  if total == length:
    # print(array[mid], '정답') 
    return array[mid]
  elif total > length:
    mid = array[mid + 1] # 다음 인덱스 값으로 설정
    return findHeight(array, num, length, mid)
  elif total < length:
    mid = array[mid - 1] # 이전 인덱스 값으로 설정
    return findHeight(array, num, length, mid)

findHeight(rice, n, m, mid)

# 35-40분정도 소요(문제 해결 아이디어 짜는 시간 포함)

