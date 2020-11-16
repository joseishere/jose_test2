# getWords.py
# gets all of the words from a file
def fromFile(fileName):
    f = open(fileName, 'r')
    finalList = f.read().split('\n')
    return finalList

def main():
    print(fromFile('testInputs.txt'))


if __name__ == '__main__':
    main()
