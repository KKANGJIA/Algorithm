# 2) 입출력 순서에 대한 언급이 있다면, stack , queue 이라 간파하고 pop 으로 풀려고 해보기
# 이해완료, 시간이 흐르고 풀 수 있는 지 확인하기!
import math


def solution(progresses, speeds):
    answer = []
    # remain = [100 - progresses[i] for i in range(len(progresses))]
    # print(remain)  # [7, 70, 45]

    # days = [math.ceil(remain[i] / speeds[i]) for i in range(len(remain))]
    # print(days)  # [7, 3, 9]

    # 옷의 지퍼(zipper)처럼 두 그룹의 데이터를 서로 엮어주는 파이썬의 내장 함수 zip()
    check = [math.ceil((100 - x)/y) for x, y in zip(progresses, speeds)]
    # print(check)  # [7, 3, 9]

# 스택, 큐 공부하기 # 2번 입출력에서 막혔음
# 다른 사람 풀이 참고
    while len(check) > 0:

        # 자기 자신 포함
        cnt = 1
        a = check.pop(0)  # 7
        check1 = check.copy()  # 얕은(데이터) 복사 [3, 9]
        for i in range(len(check)):
            if a >= check[i]:
                cnt += 1
                # 계산한 내역은 빼줘야 함
                check1.pop(0)
            else:  # 7보다 9가 더 크니까 반복문을 종료하고 cnt는 1에서 끝
                break
        answer.append(cnt)  # 위에서 cnt2 와 1을 각각 리스트에 저장한다
        check = check1.copy()  # check에 비어버린 check1릿스트를 대입해서 반복문을 종료한다?

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))


''' 다른 풀이 참고
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
'''
