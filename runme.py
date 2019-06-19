from decrypt import *
from encrypt import *

type = input('Would you like to decode or encode?'+'\n')
if type == 'decode':
    key = input('What is the encryption key?'+'\n')

    message = input('Please input the encoded message!'+'\n')
        
    if len(message) == 1:
        decryptchar(message,key)

    else:
        i = 0
        for i in range(0, len(message)):
            twooverride = true
            threeoverride = true
            fouroverride = true
            fiveoverride = true
            sixoverride = true
            sevenoverride = true
            stop = false

            character0 = str(message[i])
            character1 = str(message[i+1])
            if i+2 < len(message):
                character2 = str(message[i+2])
                twooverride = false
            if i+3 < len(message):
                character3 = str(message[i+3])
                threeoverride = false
            if i+4 < len(message):
                character4 = str(message[i+4])
                fouroverride = false
            if i+5 < len(message):
                character5 = str(message[i+5])
                fiveoverride = false
            if i+6 < len(message): 
                character6 = str(message[i+6])
                sixoverride = false
            if i+7 < len(message):
                character7 = str(message[i+7])
                sevenoverride = false

            if character0 != '' and character1 == '':
                decryptchar(character0, key)
                i+=2
            elif character0 != '' and character1 != '':
                if twooverride:
                    newmessage = character0+character1
                    decryptchar(newmessage, key)
                elif character2 == '':
                    newmessage = character0+character1
                    decryptchar(newmessage, key)
                    i+=3
                else:
                    if threeoverride:
                        newmessage = character0+character1+character2
                        decryptchar(newmessage, key)
                    elif character3 == '':
                        newmessage = character0+character1+character2
                        decryptchar(newmessage, key)     
                        i+=4
                    else:
                        if fouroverride:
                           newmessage = character0+character1+character2+character3 
                           decryptchar(newmessage, key)     

                        elif character4 == '':
                           newmessage = character0+character1+character2+character3 
                           decryptchar(newmessage, key)     
                           i+=5
                        else:
                            if fiveoverride:
                                newmessage = character0+character1+character2+character3+character4
                                decryptchar(newmessage, key)     

                            elif character5 =='':
                                newmessage = character0+character1+character2+character3+character4
                                decryptchar(newmessage, key)     
                                i+=6
                            else:
                                if sixoverride:
                                    newmessage = character0+character1+character2+character3+character4+character5
                                    decryptchar(newmessage, key)     
                                    
                                elif character6== '':
                                    newmessage = character0+character1+character2+character3+character4+character5
                                    decryptchar(newmessage, key)     
                                    i+=7
                                else:
                                    if sevenoverride:
                                        newmessage = character0+character1+character2+character3+character4+character5+character6
                                        decryptchar(newmessage, key)                                            
                                    elif character7== '':
                                        newmessage = character0+character1+character2+character3+character4+character5+character6
                                        decryptchar(newmessage, key)                                            
                                        i+=8
                                    else:
                                         newmessage = character0+character1+character2+character3+character4+character5+character6+character7
                                         decryptchar(newmessage,key)
                                         i+=9
elif type == 'encode':
    key = input('What is the encryption key?'+'\n')
    message = input('What is the message you would like to encode?'+'\n')

    for i in range(0, len(message)):
        if message[i] != '':
            encryptchar(message[i], key)
        else:
            print('\n')
