def solution(record):
    record_split = [record[i].split()
                    for i in range(len(record))]  # 2차원 배열로 쪼개기
    uid_nick_dict = {}  # 키: 유저아이디, 값: 닉네임
    result = []  # 메세지를 출력할 배열

    for i in range(len(record_split)):
        if record_split[i][0] == 'Enter':
            uid_nick_dict[record_split[i][1]] = record_split[i][2]
            result.append(uid_nick_dict[record_split[i][1]] + '님이 들어왔습니다.')

        elif record_split[i][0] == 'Leave':
            result.append(uid_nick_dict[record_split[i][1]] + '님이 나갔습니다.')
            del uid_nick_dict[record_split[i][1]]

        elif record_split[i][0] == 'Change':
            uid_nick_dict[record_split[i][1]] = record_split[i][2]
            print(uid_nick_dict)  # {'uid4567': 'Ryan', 'uid1234': 'Prodo'}

    return result

# dict으로 풀 수 있다는 문제 해결 방법은 찾았지만 아직 구현단계에서 논리적인 단계로 구현하는 게 어려운 듯 함
# 각 단계를 나눠서 논리적으로 구현하는 방법 찾아야 할 듯
# 무조건 if로만 작성하지말고 조건을 어떻게 반복해서 쉬운 코드를 짤 수 있는가를 고민하자!


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))
