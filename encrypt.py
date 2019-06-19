from sympy import *
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

def shift(char):
    global additionshift
    global multiplicationshift
    global powershift
    global letter
    global value
    global finalvalue

    letter = char
    getlettervalue(letter)
    if multiplicationshift == 0 and powershift == 0:
        finalvalue = value + additionshift
    elif powershift == 0:
        finalvalue = value * multiplicationshift
    else:
        finalvalue = multiplicationshift * (value ** powershift)

    backtoletter(finalvalue)

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
        letter = 'a'
    elif lettervalue == 2:
        letter = 'b'
    elif lettervalue== 3:
        letter = 'c'
    elif lettervalue== 4:
        letter = 'd'
    elif lettervalue== 5:
        letter = 'e'
    elif lettervalue== 6:
        letter = 'f'
    elif lettervalue== 7:
        letter = 'g'
    elif lettervalue== 8:
        letter = 'h'
    elif lettervalue== 9:
        letter = 'i'
    elif lettervalue== 10:
        letter = 'j'
    elif lettervalue== 11:
        letter = 'k'
    elif lettervalue== 12:
        letter = 'l'
    elif lettervalue== 13:
        letter = 'm'
    elif lettervalue== 14:
        letter = 'n'
    elif lettervalue== 15:
        letter = 'o'
    elif lettervalue== 16:
        letter = 'p'
    elif lettervalue== 17:
        letter = 'q'
    elif lettervalue== 18:
        letter = 'r'
    elif lettervalue== 19:
        letter = 's'
    elif lettervalue== 20:
        letter = 't'
    elif lettervalue== 21:
        letter = 'u'
    elif lettervalue== 22:
        letter = 'v'
    elif lettervalue== 23:
        letter = 'w'
    elif lettervalue== 24:
        letter = 'x'
    elif integer== 25:
        letter = 'y'
    elif lettervalue== 26:
        letter = 'z'
    elif lettervalue > 26:
        lettervalue = lettervalue - 26
        print('z')
        backtoletter(lettervalue)

def encryptchar(char, string):
    global encryptionkey
    global realencryption
    global letter
    global finalletter
    global multiplicationshift
    global additionshift
    global powershift

    encryptionkey = string
    letter = char
    getshifttype(encryptionkey)
    shift(letter)
    print(letter)
    print('')









