#!/bin/python3

dict1 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5,
        'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10,
        'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15,
        'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20,
        'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26}

dict2 = {0 : 'z', 1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e',
        6 : 'f', 7 : 'g', 8 : 'h', 9 : 'i', 10 : 'j',
        11 : 'k', 12 : 'l', 13 : 'm', 14 : 'n', 15 : 'o',
        16 : 'p', 17 : 'q', 18 : 'r', 19 : 's', 20 : 't',
        21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x', 25 : 'y'}

def decrypt(letter,shift):
    decipher = ""
    if(letter != '_' and letter != '?'):
        num = ( dict1[letter] - shift + 26) % 26
        decipher += dict2[num]
    elif(letter == '?'):
        decipher += '?'
    else:
        decipher += '_'

    return decipher


p = list("ujp?_oHy_lxiu_zx_uve")

flag = "corctf{"

flag += decrypt(p[0],2)
flag += decrypt(p[1],5)
flag += decrypt(p[2],11)
flag += decrypt(p[3],13)
flag += decrypt(p[4],17)
flag += decrypt(p[5],23)
flag += decrypt(p[6].lower(),29).upper()
flag += decrypt(p[7],29)
flag += decrypt(p[8],37)
flag += decrypt(p[9],37)
flag += decrypt(p[10],41)
flag += decrypt(p[11],47)
flag += decrypt(p[12],53)
flag += decrypt(p[13],53)
flag += decrypt(p[14],59)
flag += decrypt(p[15],61)
flag += decrypt(p[16],67)
flag += decrypt(p[17],71)
flag += decrypt(p[18],73)
flag += decrypt(p[19],79)

flag += "}"

print(flag)
