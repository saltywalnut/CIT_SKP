num = 5

def factorial (num):
    result = 1
    while num > 0:
        result = result * num
        num -= 1
    return result

factorial (num)

userNum = 1

def fact_recurse(num):
    if num == 1 :
        return 1
    else:
        return num * fact_recurse(num -1)

def fibo_iterate(num):
    first = 1
    second = 1

    while num > 2:
        temp = second
        second = first + second
        first = temp
        num -=1
    return second

def fibo_recurse(num):
    if num == 1 or num == 2 :
        return 1
    else:
        return fibo_recurse(num - 1) + fibo_recurse(num - 2)

while userNum != -1 :
    userNum = int ( input ( "type a number : "))
    print ("Iteration : " + str (fibo_iterate(userNum)))
    print ("recursion : " + str (fibo_recurse (userNum)))
