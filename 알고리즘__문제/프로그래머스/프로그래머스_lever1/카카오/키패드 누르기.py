def solution(numbers, hand):
    result = ''
    prev_left = 10
    prev_right = 12

    for elem in numbers:
        if elem in [1, 4, 7]:
            result += 'L'
            prev_left = elem
        elif elem in [3, 6, 9]:
            result += 'R'
            prev_right = elem
        else:
            elem = 11 if elem == 0 else elem

            absL = abs(elem-prev_left)
            absR = abs(elem-prev_right)

            # 3으로 나눈 몫과 나머지를 더해서 키패드의 거리를 구하기
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                result += 'R'
                prev_right = elem
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                result += 'L'
                prev_left = elem
            else:
                if hand == 'left':
                    result += 'L'
                    prev_left = elem
                else:
                    result += 'R'
                    prev_right = elem

    return result


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers, hand))
