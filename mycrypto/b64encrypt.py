# -*- coding: utf-8 -*-
code = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def b64encrypt(src, msg):
    from libnum import n2s, s2n
    from base64 import b64encode
    lines = 0
    '''
    for i in range(len(src)):
        if src[i] == '\n':
            lines += 1
    length = s2n(msg).bit_length()
    if lines < 2 * length:
        return 'Failed'
    '''
    put = []
    src = src.split('\n')
    container = 0
    for i in range(len(src)):
        src[i] += '\n'
        length = len(src[i])
        container += - (length % 3) % 3 * 2
    bins = bin(s2n(msg))[2:]
    bins = '0' * (- (len(bins) % 8)  % 8) + bins
    print container, len(bins)
    assert container >= len(bins)
    bins += '0' * (container - len(bins))
    index = 0
    for i in range(len(src)):
        cur = b64encode(src[i])
        src[i] = cur
        equal = 0
        if cur[-1] == '=':
            equal += 1
            if cur[-2] == '=':
                equal += 1
        if equal == 0:
            continue
        if index >= container:
            break
        add = int(bins[index: index + 2 * equal], 2)
        index += 2 * equal
        change = cur[- equal - 1]
        assert code.index(change) ^ add == code.index(change) + add
        change = code[code.index(change) ^ add]
        src[i] = src[i][0: - equal - 1] + change + '=' * equal
    return '\n'.join(src)
