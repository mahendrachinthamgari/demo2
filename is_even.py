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