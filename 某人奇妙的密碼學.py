#某人奇妙的密碼學
def code(text,key,aim):
    result=''
    for i in range(len(text)):
        if ord(text[i])==32:
            result+=' '
        else:
            order=ord(text[i])-65
            if aim=='encrypt':
                newcode=(order+key)%26
            elif aim=='decrypt':
                newcode=(order-key)%26
            result+=chr(newcode+65)
            print(newcode+65)
    print(result)
code('TODAY IS A GOOD DAY',7,'encrypt')
code('AVKHE PZ H NVVK KHF',7,'decrypt')
code('z',7,'encrypt')

#print((ord('y')-65+7)%26)
#print(chr((ord('y')-65+7)%26))