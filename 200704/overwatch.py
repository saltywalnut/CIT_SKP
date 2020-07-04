rating = -30000
if rating>5000 or rating<0:
    print ("Error")
if rating > 4000 and rating <5000:
    print ("Grand Master")
elif rating < 3500 and rating > 3000:
    print ("Master")
elif rating < 3000 and rating >2500:
    print ("Diamond")
elif rating < 2500 and rating >2000:
    print ("Platinum")
elif rating < 2000 and rating >1500:
    print ("Gold")
elif rating < 1500 and rating >1000:
    print ("Silver")
elif rating < 1000 and rating >500:
    print ("Bronze")\

rating = 1800

if rating < 0 or rating > 5000:
    print ("Error")
elif rating > 4000 :
    print ("GM")
elif rating > 3500:
    print ("M")
elif rating > 3000:
    print ("D")
elif rating > 2500:
    print ("P")
else :
    print ("BSG")
