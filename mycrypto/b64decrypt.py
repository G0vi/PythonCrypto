def b64steg(src):
    f = open(src, 'r')
    string = f.read()
    lis = string.split('\n')
    src = ''
    for i in range(26):
        src += chr(65 + i)
    for i in range(26):
        src += chr(97 + i)
    for i in range(10):
        src += chr(ord('0') + i)
    src += '+/'
    ans = ''
    for eve in lis:
        equal = 0
        length = len(eve)
        if length:
            while length - equal - 1 >= 0 and eve[-equal - 1] == '=':
                equal += 1
            cur = eve[-equal - 1]
            place = src.index(cur)
            bit = bin(place)[2:].rjust(6, '0')
            if equal == 1:
                ans += bit[-2:]
            if equal == 2:
                ans += bit[-4:]
    final = ''
    for i in range(0, len(ans), 8):
        final += chr(int(ans[i:i + 8], 2))
    end = len(final) - 1
    while ord(final[end]) < 32 or ord(final[end]) > 127:
        end -= 1
    return final[:end + 1]

