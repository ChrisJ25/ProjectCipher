from decrypt import *
from encrypt import *

type = input('Would you like to decode or encode?'+'\n')
if type == 'decode':
    key = input('What is the encryption key?'+'\n')

    count= input('How many sets of adjacent characters is your message?'+'\n')

    for i in range(0,int(count)):
        message = input('Please input the next set of adjacent characters!'+'\n')
        decryptchar(message,key)
        i= i+1
    
elif type == 'encode':
    key = input('What is the encryption key?'+'\n')
    message = input('What is the message you would like to encode?'+'\n')

    for i in range(0, len(message)):
        if message[i] != '':
            encryptchar(message[i], key)
        else:
            print('\n')
