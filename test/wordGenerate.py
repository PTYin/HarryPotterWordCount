f = open("book.txt", 'w')
for k in range(0x100000):
    for i in range(1, 11):
        f.write(str(i))
    f.write("\r\n")
f.close()
