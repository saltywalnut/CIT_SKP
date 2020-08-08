def mean4(mw, sk, yc, jk):
    sum = mw + sk + yc + jk
    return sum/4

# print (mean4(7,8,9,0))
# print ( mean4(3, 8, mean4(1,3,2,6), 9) )

def teemoDies (damage):
    teemoHealth = 500
    if (teemoHealth > damage):
        return "alive"
    else:
        return "dead"

damage = int (input ("type the damage you dealt to teemo : ") )
print (teemoDies(damage))

print (teemoDies)
