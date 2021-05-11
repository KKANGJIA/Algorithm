import datetime

# a = year.month  # 월
# b = year.day  # 일
# print(a, b)  # 1 1


def solution(a, b):
    weekends = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    year = datetime.date(2016, a, b)
    # print(year)  # 2016-01-01
    # print(int(year.weekday())) # 0부터 월요일 일요일 6
    return weekends[int(year.weekday())]


print(solution(5, 29))
