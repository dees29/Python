def pyramid(rows):
    for i in range(0,rows):
        print((rows-i-1)*" " + (i+1)*"* ")
    for j in range(rows-1,0,-1):
        print((rows-j)*" " + (j)*"* ")

pyramid(5)
