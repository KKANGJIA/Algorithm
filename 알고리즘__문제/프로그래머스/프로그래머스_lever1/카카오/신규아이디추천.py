def solution(new_id):
    if new_id.isupper() == True:
        new_id.lower()
        print(new_id)
    if new_id.count('.') > 1:
        set(new_id)
        print(new_id)
    if new_id[0] == '.':
        new_id.pop(new_id[0])
        print(new_id)
    if new_id[-2:-1] == '.':
        new_id.pop(new_id[-2:-1])
        print(new_id)
    if new_id == '':
        new_id += 'a'
        print(new_id)
    if len(new_id) > 15:
        new_id = new_id[:16]
        print(new_id)
        if new_id[-2:-1] == '.':
            new_id.pop(new_id[-2:-1])
            print(new_id)
    if len(new_id) <= 2:
        new_id += new_id[len(new_id)-2:]
        print(new_id)

    return new_id


new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))
