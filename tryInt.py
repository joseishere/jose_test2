# tryInt.py
hex_vals = {
    'a':'a',
    'A':'A',
    'b':'b',
    'B':'B',
    'c':'c',
    'C':'C',
    'd':'d',
    'D':'D',
    'e':'e',
    'E':'E',
    'f':'f',
    'F':'F',
}
def intChecker(arr):
    foundu = False
    foundU = False
    size = len(arr)
    try:
        letterFound = arr[2:].find(next(filter(str.isalpha, arr[2:])))
    except:
        letterFound = -1
    #print(letterFound)
    if(size < 2):
        return False
    if(arr[0] == '0' and arr[1] == 'x' or arr[1] == 'X'):

        xo={
            'a' : 'u',
            'b' : 'U',
            'c' : 'l',
            'd' : 'L'
        }

        size = len(arr) - 1
        suffix = [None] * len(arr)

        while(size >= 0):
            #print(size)
            if(arr[size] in xo.values()):
                suffix[size] = arr[size]
            else:
                break
            size -= 1
        #print(suffix)
        temp = ''
        for each in suffix:
            if(each is not None):
                temp += each
        #print(temp)
        #print("final size : " + str(size))

        if(size != len(arr) - 1):
            for char in arr[2:size+1]:
                #print(char)
                if(char.isnumeric() or char in hex_vals.values()):
                    #print('what')
                    pass
                else:
                    print('ere')
                    return False
            return (True and checkEnd(arr, size+1, 'hex'))
        else:
            return True

    elif(arr[0] == '0' and arr[1] < '8'):
        if(letterFound != -1):
            for char in arr[2:letterFound+2]:
                #print(char)
                if(char < '8'):
                    pass
                else:
                    #print('ere')
                    return False
            return (True and checkEnd(arr, letterFound+2, 'oct'))
        else:
            return True
    elif(arr[0] != 0):
        if(letterFound != -1):
            for char in arr[2:letterFound+2]:
                #print(char)
                if(char.isnumeric()):
                    pass
                else:
                    #print('ere')
                    return False
            return (True and checkEnd(arr, letterFound+2, 'dec'))
        else:
            return True
    else:
        return False

def checkEnd(arr, startLetter, type):
    endString = arr[startLetter:]
    #print(endString, "end string")
    dec_endings = {
        'u':'u',
        'l':'l',
        'ul':'ul',
        'LL':'LL',
        'ull':'ull',
    }
    hex_endings = {
        'u':'u',
        'l':'l',
        'uL':'uL',
        'll':'ll',
        'uLL':'uLL',
    }
    oct_endings = {
        'u':'u',
        'l':'l',
        'UL':'UL',
        'll':'ll',
        'Ull':'Ull',
    }


    whereToLook = str(type) + "_endings"
    #print(whereToLook)
    if(type == 'dec'):
        if(endString in dec_endings.values()):
            #print('checkend returned true')
            return True
        else:
            return False
    elif(type == 'hex'):
        if(endString in hex_endings.values()):
            #print('checkend returned true')
            return True
        else:
            return False
    elif(type == 'oct'):
        if(endString in oct_endings.values()):
            #print('checkend returned true')
            return True
        else:
            return False
    else:
        return False


def main():

    words = ["28","4000000024u","2000000022l","4000000000ul","9000000000LL","900000000001ull","024","04000000024u","02000000022l","04000000000UL", "044000000000000ll","044400000000000001Ull", "0x2a", '0XA0000024uu', '0x20000022ll','0XA0000021uLLL','0x8a000000000000lll','0x8A40000000000010uLLL']

    for word in words:
        if(intChecker(word)):
            print(word + " is valid")
        else:
            print(word + " is not valid")



if __name__ == "__main__":
    main()
