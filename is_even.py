def is_even(n):
    print("This is :")
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"

def push(arr):
    l = []
    for i in range(len(arr)):
        l.append(arr[i])
    return arr

def fun():
    print("you ar funny")
    return 0

if __name__ == '__main__':
    n = int(input("Enter the number :"))
    print(is_even(n))
    fun()