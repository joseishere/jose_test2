# tryChar.py
symbols ={
    '~' : '~' ,
    '`' : '`' ,
    '!' : '!' ,
    '@' : '@' ,
    '#' : '#' ,
    '$' : '$' ,
    '%' : '%' ,
    '^' : '^' ,
    '&' : '&' ,
    '*' : '*' ,
    '(' : '(' ,
    ')' : ')' ,
    '-' : '-' ,
    '_' : '_' ,
    '+' : '+' ,
    '=' : '=' ,
    '{' : '{' ,
    '[' : '[' ,
    '}' : '}' ,
    ']' : ']' ,
    '|' : '|' ,
    ':' : ':' ,
    ';' : ';' ,
    '<' : '<',
    ',' : ',',
    '>' : '>',
    '.' : '.',
    '?' : '?',
}

after_slash = {
    'b':'b',
    'f':'f',
    'n':'n',
    'r':'r',
    '"':'"',
    '\\':'\\',
    "'":"'",
    'v':'v',
    'a':'a',
    '?':'?',
    'N':'N',
    'X':'X',
    't':'t',
}


def charChecker(arr):
    # this is very similar to the java string, so took the same algorithm from my java string and adapted it here
    # i think we first need to handle the simplest case just making sure that we have the correct open and close
    size = len(arr)
    count = 0
    # need this to handle the /XN
    isX = False

    # we cant have an empty string or 'a
    # and we know we can't have anything more than 5
    if(size >= 5 or size < 3):
        return False
    # print(arr[0], arr[-1])

    if((arr[0] == '"' and arr[-1] == '"') or (arr[0] == "'" and arr[-1] == "'")):

# don't need to check first letter since we know what it is
# now we need to loop through the string and if we have a slash
# we need to know that the next number, in this case arr[num] is a valid value
# and we need to make sure that we only have an even number of slashes bc \\\
# is not valid even though you can have a \ after a \
        num = 1
        for letter in arr[1:-1]:
            #print(letter, "printing letter hereeee")
            num +=1
            if(letter.isalnum() or letter in symbols.values()):
                pass
            elif(letter == '\\'):
                count+=1
                # print(count)
                if(isX):
                    if(arr[num] != 'N'):
                        return False
                elif(arr[num] in after_slash.values()):
                    #print(str(size) + " size")
                    if(arr[num] == 'X'):
                        isX = True
                    if(num < size-1):
                        count+=-1
                        #print(count)
                elif(arr[num] not in after_slash.values()):
                    return False
            else:
                pass
    else:
        return False
    if(count == 0):
        return True

    return True


def main():

    words = ["\'1\'", "\'!\'", "\"$\"", "\'\t\'", "\'\?\'", "\'\\\'", "\'\f\'", "\'\XN\'", "\']\'", "\'n\'", '\'e\"' , "v\'v\'",  '"024"']

    for word in words:
        if(charChecker(word)):
            print(word + " is valid")
        else:
            print(word + " is not valid")

if __name__ == "__main__":
    main()
