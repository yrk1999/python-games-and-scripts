msg = list(input(str("Enter binary string:")))
if(len(msg) % 8 == 0):
    length = len(msg)
    decoded  = []
    for i in range(len(msg)):
        length = len(msg)
        sub = list(msg[:8])
        del msg[:8]
        wordval = 0
        for x in range(len(sub)):
            if int(sub[x]) == 1:
                if x is 0:
                    wordval += 128
                elif x is 1:
                    wordval += 64
                elif x is 2:
                    wordval += 32
                elif x is 3:
                    wordval += 16
                elif x is 4:
                    wordval += 8
                elif x is 5:
                    wordval += 4
                elif x is 6:
                    wordval += 2
                elif x is 7:
                    wordval += 1
        if wordval != 0:
            decoded.append(chr(wordval))
    for i in range(len(decoded)):
        print(decoded[i],end='')
    print()
else:
    print("Enter valid string")