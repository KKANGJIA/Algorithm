def solution(money, cost):
    floor_dict = {}

    for i in range(len(cost)):
        floor_dict[i+1] = cost[i]
        # print(floor_dict) # {1: 0, 2: 900, 3: 0, 4: 200, 5: 150, 6: 0, 7: 30, 8: 50}
        for j in range(len(cost)):
            if money > sum(cost[i:j]):
                max(sum(cost[i:j]))


money = 420
cost = [0, 900, 0, 200, 150, 0, 30, 50]

print(solution(money, cost))
