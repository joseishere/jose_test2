# tryFloat.py
import re

def floatChecker(arr):

    # I did this one with regex after people started to talk about how they used it in the plc group chat
    # of course all of the other ones I didn't do with regex bc they were already done
    # really wish i would have done everything with regex
    # also I used this website to help me build the regex string
    # it is really well made and you should donate to help keep it running
    # the website is : https://regex101.com

    regexBase = r"(-)?(\d)*(.)?\d+(e|E)?(-)?\d(l|L|f|F)?"

    if(re.fullmatch(regexBase, arr)):
        # print('is valid')
        return True
    else:
        return False


def main():

    words = ["23.75", "0.59201E1", "1312221215e-2", "-2.5e-3", "15E-4", "121.0L", "122.0F", "1x0.0F", ".02ef3", "0.01ee1", "0.5e1lf", "69e--2"]


    for word in words:
        if(floatChecker(word)):
            print(word + " is valid")
        else:
            print(word + " is not valid")


if __name__ == "__main__":
    main()
