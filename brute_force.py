import time
import itertools

def tryCrackPassword(passwordSet, stringTypeSet):
    start = time.time()
    chars = stringTypeSet
    iterations = 0
    for i in range(1,9):
        for letter in itertools.product(chars, repeat=i):
            iterations += 1
            letter = ''.join(letter)
            if letter == passwordSet:
                end = time.time()
                total_time = end - start
                return (iterations, total_time)
            
def main():
    password = input("Password >")
    stringType = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    tries, timeAmount = tryCrackPassword(password, stringType)
    print((password, tries, timeAmount))

if __name__ == "__main__":
    main()
