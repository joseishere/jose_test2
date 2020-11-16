# tryOperator.py
def operatorChecker(op):
    # we need to make sure that we get an operator and not empty string
    # and that the length of the operator is never more than 4
    if(len(op) > 4):
        return False

    # now we just see what it is

    if (op == '+' ):
        return True
    elif (op == '-' ):
        return True
    elif (op == '='):
        return True
    elif (op == '-'):
        return True
    elif (op == '/'):
        return True
    elif (op == '*'):
        return True
    elif (op == '%'):
        return True
    elif (op == '{'):
        return True
    elif (op == '}'):
        return True
    elif (op == '('):
        return True
    elif (op == ')'):
        return True
    elif (op == '++'):
        return True
    elif (op == '--'):
        return True
    elif (op == '&&'):
        return True
    elif (op == '||'):
        return True
    elif (op == '!'):
        return True
    else:
        return False

def main():
    words = ['+', '-', '/', '%', '+-', '', 'faill', '$$', '1']

    for word in words:
        if(operatorChecker(word)):
            print(word + " is valid")
        else:
            print(word + " is not valid")

if __name__ == "__main__":
	main()
