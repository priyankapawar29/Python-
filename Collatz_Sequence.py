""" The Collatz Sequence"""
def Collatz(numm):
    if numm % 2 == 0:
        result = numm // 2
        return result
    else:
        result = 3 * numm + 1
        return result

try:
    num = int(input("Enter the number: "))
    while num > 1:
        num = Collatz(num)
        print (num)

except ValueError:
    print("Please enter number")
