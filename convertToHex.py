a = list(str(input("Enter string to be converted to hex:")))
b = []
for i in a:
	b.append(hex(ord(i)))
for i in b:
    print(i,end='')
