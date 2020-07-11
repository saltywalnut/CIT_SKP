def addThenTriple(elsa, anna):
    result = elsa + anna
    result = result * 3
    return result

# print (addThenTriple(5, 3))
# print (addThenTriple(5, addThenTriple(1,4)))

def sayHi (name):
    print ("Hi, my friend " + name)

sayHi ("Olaf")

# def sayHo ():
#     return "Ho!"
#
# print (sayHo)

def sayYay():
    print ("Yay")

sayYay()
print ( sayYay())

test = input("type your name : ")
sayHi (test)
