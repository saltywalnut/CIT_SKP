someList = ['a','e','c','d','b']


def swapList(list,i1,i2):
    temp = list[i1]
    list[i1] = list[i2]
    list[i2] = temp

swapList(someList,1,4)
print(someList)
