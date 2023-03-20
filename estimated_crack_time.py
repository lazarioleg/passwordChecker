import time
import itertools

RATE = 200
DIGITS = 10
LOWER = 26
LETTERS = 52
TOTAL = 84


def checkNum(char_nums):         
    return ((DIGITS ** char_nums) / RATE)

def checklower(char_nums):         
    return ((LOWER **  char_nums) / RATE)

def checkLetters(char_nums):
    return ((LETTERS ** char_nums) / RATE)

def checkSymbolic(char_nums):
    return ((TOTAL ** char_nums) / RATE)

def estimateTime(password):
    char_nums = len(password)
    
    if password.isdigit() == True:
        print(checkNum(char_nums))
        
    elif password.islower() == True:
        print(checkNum(char_nums))

    elif password.isalpha() == True:
        print(checkLetters(char_nums))

    else:
        print(checkSymbolic(char_nums))


def main():
    pass1 = "test"
    pass2 = "Exp1$dj"
    pass3 = "1234567890"

    estimateTime(pass1)
    estimateTime(pass2)
    estimateTime(pass3)

if __name__ == "__main__":
    main()

    

    

    

        

