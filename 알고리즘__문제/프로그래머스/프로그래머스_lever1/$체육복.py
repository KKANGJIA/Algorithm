def max_students(n, lost, reserve):
    # 빌려줄 수 있는 애는 한명 더 듣게 해줄 수 있음(안, 뒤 중 한명만 가능)
    # lost, reserve에 포함되지 않는 애도 들을 수 있음

    #  둘 다 포함되지 않는 애들 수 세고 빌려줄 수 있는 애는 2개로 쳐서 더하되 앞뒤라는 조건을 만족하면 추가하기

    cnt = n - len(reserve) - len(lost)  # 기본적으로 수업들을 수 있는 애들의 수
    print(cnt)

    borrow = []
    # 빌려줄 수 있는 지만 판단해서 수 더해주기
    for i in reserve:
        print(reserve)
        if (i - 1) in lost:
            borrow.append(i - 1)
            print(lost, borrow)
        if (i + 1) in lost:
            borrow.append(i + 1)
            print(lost, borrow)
    print(borrow)  # [4, 2]

    real_borrow = list(set(borrow))  # 중복제거
    print(real_borrow)

    for i in real_borrow:
        if i in lost:
            cnt += 1

    return cnt


print(max_students(3, [3], [1]))
