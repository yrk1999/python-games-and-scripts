inp = str(input("Enter text: "))
msg = list(inp)

text = []
for i in range(len(msg)):
    if msg[i] != ' ':
        a = bin(ord(msg[i]))
        for j in a:
            if j != 'b':
                text.append(j)
    else:
        text.append(' ')
print('"{}" in binary is:'.format(inp))

for i in range(len(text)):
    print(text[i],end='')

print()
