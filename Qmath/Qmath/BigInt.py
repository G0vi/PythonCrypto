def root(n, index):
    Length = n.bit_length()
    length = Length // index
    down = 2 ** length if Length % index != 0 else 2 ** (length - 1)
    up = 2 ** (length + 1)
    ave = (up + down) // 2
    while not (ave ** index <= n and (ave + 1) ** index > n):
        if ave ** index > n:
            up = ave - 1
        else:
            down = ave + 1
        ave = (up + down) // 2
    return ave
        
def log_int(n, index):
    li = []
    cur = n
    while cur:
        add= cur % index
        li.append(add)
        cur //= index
    return len(li) - 1
