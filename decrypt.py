import sys

def getshifttype(string):
    global additionshift
    global multiplicationshift
    global powershift
    global encryptionkey

    encryptionkey = string

    if len(encryptionkey) == 1:
        additionshift = int(encryptionkey[0])
        multiplicationshift = 0
        powershift = 0
    elif len(encryptionkey) == 2:
        multiplicationshift = int(encryptionkey[0])
        powershift = 0
        additionshift = 0
    elif len(encryptionkey) == 3:
        multiplicationshift = int(encryptionkey[0])
        powershift = int(encryptionkey[2])
        additionshift = 0

def shift(int):
    global additionshift
    global multiplicationshift
    global powershift
    global letter
    global value
    global finalvalue

    finalvalue = int
    if multiplicationshift == 0 and powershift == 0:
        finalvalue = finalvalue - additionshift
    elif powershift == 0:
        finalvalue = finalvalue / multiplicationshift
    else:
        finalvalue = (finalvalue ** 1/powershift) / multiplicationshift

def getlettervalue(char):
    global value
    if char == 'a':
        value = 1
    elif char == 'b':
        value = 2
    elif char == 'c':
        value = 3
    elif char == 'd':
        value = 4
    elif char == 'e':
        value = 5    
    elif char == 'f':
       value = 6 
    elif char == 'g':
        value = 7
    elif char == 'h':
        value = 8
    elif char == 'i':
        value = 9
    elif char == 'j':
        value = 10
    elif char == 'k':
        value = 11
    elif char == 'l':
        value = 12
    elif char == 'm':
        value = 13
    elif char == 'n':
        value = 14
    elif char == "o":
        value = 15
    elif char == "p":
        value = 16
    elif char == "q":
        value = 17
    elif char == "r":
        value = 18
    elif char == "s":
        value = 19
    elif char == "t":
        value = 20
    elif char == "u":
        value = 21
    elif char == "v":
        value = 22
    elif char == "w":
        value = 23
    elif char == "x":
        value = 24
    elif char == "y":
        value = 25
    elif char == "z":
        value = 26

def backtoletter(integer):
    global letter
    lettervalue = integer
    if lettervalue == 1:
        print('a')
    elif lettervalue == 2:
        print('b')
    elif lettervalue== 3:
        print('c')
    elif lettervalue== 4:
        print('d')
    elif lettervalue== 5:
        print('e')
    elif lettervalue== 6:
        print('f')
    elif lettervalue== 7:
        print('g')
    elif lettervalue== 8:
        print('h')
    elif lettervalue== 9:
        print('i')
    elif lettervalue== 10:
        print('j')
    elif lettervalue== 11:
        print('k')
    elif lettervalue== 12:
        print('l')
    elif lettervalue== 13:
        print('m')
    elif lettervalue== 14:
        print('n')
    elif lettervalue== 15:
        print('o')
    elif lettervalue== 16:
        print('p')
    elif lettervalue== 17:
        print('q')
    elif lettervalue== 18:
        print('r')
    elif lettervalue== 19:
        print('s')
    elif lettervalue== 20:
        print('t')
    elif lettervalue== 21:
        print('u')
    elif lettervalue== 22:
        print('v')
    elif lettervalue== 23:
        print('w')
    elif lettervalue== 24:
        print('x')
    elif integer== 25:
        print('y')
    elif lettervalue== 26:
        print('z')
  

def decryptchar(string1, string):
    global encryptionkey
    global value
    global finalvalue
    global letter

    encryptionkey = string
    i = 0
    for i in range(0, len(string1)):
        getlettervalue(string1[i])
        if i > 0:
            finalvalue = value + finalvalue
        else:
            finalvalue = value    
    getshifttype(encryptionkey)
    shift(finalvalue)
    print(' |')
    print('\ /')
    print(' v')
    backtoletter(finalvalue)

    