def solution(n, arr1, arr2):
    sum_Arr1NArr2 = []  # 두개의 지도를 겹친 새로운 지도
    ele = ''
    change_map = []  # 숫자를 기호로 변경한 새로운 지도

    # 이진수 변환
    for i in range(len(arr1)):
        arr1[i] = bin(arr1[i])[2:]  # 2진수 변환 함수 bin(), 앞에 0b 제거를 위한 슬라이싱
        arr2[i] = bin(arr2[i])[2:]

        # 두개의 지도 합치기 => 합치지 않고 따로 구할 수도 있음!
        sum_Arr1NArr2.append(int(arr1[i]) + int(arr2[i]))
        sum_Arr1NArr2[i] = str(sum_Arr1NArr2[i]).zfill(n)  # 부족한 0 채우기

    # map 숫자를 기호로 변경해서 비밀지도 완성하기
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            # 지도 각 칸의 숫자의 합이 1 또는 2면 벽인 #
            if str(sum_Arr1NArr2[i])[j:j+1] == '2' or str(sum_Arr1NArr2[i])[j:j+1] == '1':
                ele += '#'
            else:  # 합이 0이면 공간을 의미하는 공백으로 변환
                ele += ' '
        change_map.append(ele[n*i:n*(i+1)])  # n*n 출력

    return change_map


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

# n = 6
# arr1 = [46, 33, 33, 22, 31, 50]
# arr2 = [27, 56, 19, 14, 14, 10]


print(solution(n, arr1, arr2))
