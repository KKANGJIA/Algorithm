import re

# 정구표현식 공부완료


def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}

    p = re.compile('(\d+)([SDT])([*#]?)')  # 정규표현식의 정보 저장
    dart = p.findall(dartResult)  # 정규식과 매치되는 모든 문자열을 리스트 형식으로 리턴
    # print(dart) # [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]

    for i in range(len(dart)):
        if dart[i][2] == "*" and i > 0:
            dart[i-1] = dart[i-1]*2

        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    # print(dart) # [2, 8, 27]
    return sum(dart)


dartResult = '1S2D*3T'
# dartResult = '1D2S#10S'
# dartResult = '1D2S0T'
# dartResult = '1S*2T*3S'
# dartResult = '1D#2S*3S'
# dartResult = '1T2D3D#'
# dartResult = '1T2D3D#'
# dartResult = '1D2S3T*'

print(solution(dartResult))
