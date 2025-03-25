#Positive, Negative, or Zero
#Write a Python program that prompts the user to enter a number. Your program should print whether the number is positive, negative, or zero.
def main():
n= int(input("What's your number?: "))
a= PNZ(n)


def PNZ(n):
if n > 0:
    return "POSITIVE"
elif n< 0:
    return "NEGATIVE"
else :
    return "ZERO"


main()