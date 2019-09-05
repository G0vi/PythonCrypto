def xor(*src):
    if type(src)!=type(('src','a')):
        return src
    if type(src[0])==type('a'):
        length = 1
        cur = []
        for i in src:
            length = max(length, len(i))
        for i in src:
            cur.append(i.rjust(length, "0"))
        c = []

        for i in range(length):
            cur_num = 0
            for eve in cur:
                cur_num ^= int(eve[i], 2)
            c.append(str(cur_num))
        c = ''.join(c)
        return c
    if type(src[0]) == type(['a']):
        length = 1
        cur = []
        for i in src:
            length = max(length, len(i))
        for i in src:
            new_li = [0]*(length-len(i))
            new_li.extend(i)
            cur.append(new_li)
        c=[]
        for i in range(length):
            cur_num=0
            for eve in cur:
                cur_num ^= eve[i]
            c.append(cur_num)
        return c
    if type(src[0])==type(0):
        num=0
        for i in src:
            num ^= i
        return num
    else:
        return None
    
    

    
    

def Or(*src):
    if type(src)!=type(('src','a')):
        return src
    if type(src[0])==type('a'):
        length = 1
        cur = []
        for i in src:
            length = max(length, len(i))
        for i in src:
            cur.append(i.rjust(length, "0"))
        c = []

        for i in range(length):
            cur_num = 0
            for eve in cur:
                cur_num |= int(eve[i], 2)
            c.append(str(cur_num))
        c = ''.join(c)
        return c
    if type(src[0]) == type(['a']):
        length = 1
        cur = []
        for i in src:
            length = max(length, len(i))
        for i in src:
            new_li = [0]*(length-len(i))
            new_li.extend(i)
            cur.append(new_li)
        c=[]
        for i in range(length):
            cur_num=0
            for eve in cur:
                cur_num |= eve[i]
            c.append(cur_num)
        return c
    if type(src[0])==type(0):
        num=0
        for i in src:
            num |= i
        return num
    else:
        return None


def neg(src,ranges=None):
    if type(src)==type('src'):
        cur = []
        for i in range(len(src)):
            cur.append(str(int(src[i], 2) ^ 1))
        return ''.join(cur)
    if type(src)==type(1):
        return int(neg(bin(src)[2:].rjust(ranges,"0"),ranges),2)
    if type(src)==type(['src']):
        cur=[]
        for i in range(len(src)):
            cur.append(src[i]^1)
        return cur
    else:
        return None

def And(*src):
    if type(src) != type(('src', 'a')) or len(src) == 1:
        return src[0]
    if type(src[0]) == type('src'):
        length = 1
        cur = []
        for i in src:
            length = max(length, len(i))
        for i in src:
            cur.append(i.rjust(length, "0"))
        c = []
        for i in range(length):
            cur_num = 1
            for eve in cur:
                cur_num &= int(eve[i], 2)
            c.append(str(cur_num))
        c = ''.join(c)
        return c
    if type(src[0]) == type(['src']):
        length = 1
        cur = []
        for i in src:
            length = max(length, len(i))
        for i in src:
            new_li = [0] * (length - len(i))
            new_li.extend(i)
            cur.append(new_li)
        c = []
        for i in range(length):
            cur_num = 1
            for eve in cur:
                cur_num &= eve[i]
            c.append(cur_num)
        return c
    if type(src[0]) == type(1):
        ans = src[0]
        for i in src:
            ans &= i
        return ans
    else:
        return None
            
def Add(*src):
    length = 1
    ans = 0
    for i in src:
        length = max(length, len(i))
        ans += int(i, 2)
    ans = ans & (2 ** length - 1)
    return bin(ans)[2 : ].rjust(length, "0")
    
    
