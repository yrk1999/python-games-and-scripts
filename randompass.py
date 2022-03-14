from random import choice, shuffle
charset = ['b', 'Y', 'x', '^', 'W', 'S', 'F', '=', 'z', 'U', 't', '@', '9', 'g', 'M', 'w', '8', 'T', '6', 'c', 'y', 'Q', '1', 's', '$', '2', '+', '"', 'E', 'm', 'B', 'N', '3', 'd', 'u', 'Z', 'C', '7', 'h', '`', 'i', 'R', 'V', '!', "'", '4', 'H', '-', 'D', '&', '/', '0', 'J', 'k', 'X', '#', 'A', 'l', 'L', 'O', '_', 'f', '.', ',', 'p', 'n', 'j', 'r', '*', 'P', 'G', 'I', 'v', 'a', 'q', '5', 'K', 'o', '%', '~', 'e']

for i in range(50):
    shuffle(charset)
site_name = str(input("Enter site name:"))
length = int(input("Enter value:"))
char_copy = charset
x = []
for i in range(length):
    x.append(choice(char_copy))

for i in range(len(x)):
    print(x[i],end='')
try:
    passfile = open('passfile.txt','a')
    passfile.write(site_name+':')
    passfile.writelines(x)
    passfile.write('\n\n')
except FileNotFoundError:
    passfile = open('passfile.txt','w')
    passfiel.write(site_name+':')
    passfile.writelines(x)
    passfile.write('\n\n')
print()
