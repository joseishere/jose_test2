# tryJava.py
after_slash = {
    't':'t',
    'r':'r',
    'n':'n',
    'f':'f',
    '"':'"',
    '\\':'\\',

}

def javaChecker(arr):
    # i think we first need to handle the simplest case just making sure that we have " "
    size = len(arr)
    count = 0
    preCount = 0
    if(size < 3):
        return False
    for letter in arr:
        if(letter == '\\'):
            preCount+=1

    if(arr[0] == "'" and arr[1] != "\\" and arr[2] == "'" and len(arr) == 3 ):
        return True
# this is so that we know that the string starts and ends with quotation mark
    if(arr[0] == '"' and arr[-1] == '"'):
# don't need to check first letter since we know what it is
# now we need to loop through the string and if we have a slash
# we need to know that the next number, in this case arr[num] is a valid value
# and we need to make sure that we only have an even number of slashes bc \\\
# is not valid even though you can have a \ after a \
        num = 1
        for letter in arr[1:-1]:
            num +=1
            if(letter == '\\'):
                count+=1
                # print(count)
                if(arr[num] in after_slash.values()):
                    if(num < size-1):
                        count+=-1
                        # print(count)
                if(arr[num] not in after_slash.values()):
                    return False
    if(count != 0):
        return False

    return True


def main():
    # the way this works is if you copy and paste my output into a java compiler, these strings will be valid
    # this is due to how the strings go into the function but it is what it is
    words = ["'a'", '"string?"', '"string\t"', '"str\\"', '"stri\\"s"', '"st\\"ri\\"s"', "valid??@123", '"val33\\{1!@#$%"']

    for word in words:
        if(javaChecker(word)):
            print(word + " is valid")
        else:
            print(word + " is not valid")

if __name__ == '__main__':
    main()
