import base64
from libnum import *
import decimal
#import socket
def oracle(c1,hostname,port,even,odd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect((hostname, port))
    s.recv(1024)
    s.send(hex(c1)[2:].strip("lL") + '\n')
    res = s.recv(1024).strip()
    s.close()
    if res == even: return 0
    if res == odd:
        return 1
    else:
        assert (0)
def partial(c, n,hostname,port,even,odd):
    k = n.bit_length()
    decimal.getcontext().prec = k  # allows for 'precise enough' floats
    lower = decimal.Decimal(0)
    upper = decimal.Decimal(n)
    for i in range(k):
        possible_plaintext = (lower + upper) // 2
        # lower==0 when i<1809
        flag = oracle(c,hostname,port,even,odd)
        if not flag:
            upper = possible_plaintext  # plaintext is in the lower half
        else:
            lower = possible_plaintext  # plaintext is in the upper half
        c = (c * c_of_2) % n  # multiply y by the encryption of 2 again
        '''if i%100==0:
            print c'''
    return int(upper)
def LSB(c,e,n,hostname,port,even,odd):
    c_of_2=pow(2,e,n)
    m=partial((c*c_of_2)%n,n,hostname,port,even,odd)
    return n2s(m)



'''
hostname = '111.198.29.45'
port = 47161
n=0x0b765daa79117afe1a77da7ff8122872bbcbddb322bb078fe0786dc40c9033fadd639adc48c3f2627fb7cb59bb0658707fe516967464439bdec2d6479fa3745f57c0a5ca255812f0884978b2a8aaeb750e0228cbe28a1e5a63bf0309b32a577eecea66f7610a9a4e720649129e9dc2115db9d4f34dc17f8b0806213c035e22f2c5054ae584b440def00afbccd458d020cae5fd1138be6507bc0b1a10da7e75def484c5fc1fcb13d11be691670cf38b487de9c4bde6c2c689be5adab08b486599b619a0790c0b2d70c9c461346966bcbae53c5007d0146fc520fa6e3106fbfc89905220778870a7119831c17f98628563ca020652d18d72203529a784ca73716db
c=0x4f377296a19b3a25078d614e1c92ff632d3e3ded772c4445b75e468a9405de05d15c77532964120ae11f8655b68a630607df0568a7439bc694486ae50b5c0c8507e5eecdea4654eeff3e75fb8396e505a36b0af40bd5011990663a7655b91c9e6ed2d770525e4698dec9455db17db38fa4b99b53438b9e09000187949327980ca903d0eef114afc42b771657ea5458a4cb399212e943d139b7ceb6d5721f546b75cd53d65e025f4df7eb8637152ecbb6725962c7f66b714556d754f41555c691a34a798515f1e2a69c129047cb29a9eef466c206a7f4dbc2cea1a46a39ad3349a7db56c1c997dc181b1afcb76fa1bbbf118a4ab5c515e274ab2250dba1872be0
e=0x10001
c_of_2=pow(2,e,n)
m=partial((c * c_of_2) % n, n)
print n2s(m)
'''
