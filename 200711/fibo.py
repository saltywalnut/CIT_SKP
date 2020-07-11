number = 1
newnumber = 1

while newnumber < 100000:
    temp = number
    number = newnumber
    newnumber = temp + newnumber
    print (newnumber)
