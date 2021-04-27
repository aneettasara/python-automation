# INPUT FILE
f1 = open("ip.txt","r")
# OUTPUT FILE for P
f2 = open("op_P.txt","w")
# OUTPUT FILE for F
f3 = open("op_F.txt","w")

for line in f1:
    word = line.split()
    if word[2] == 'P':
        f2.write(line)
    else:
        f3.write(line)

f1.close()
f2.close()
f3.close()
