class Food:
    calories = 100 #property

    def __init__(gfbvc, cal, tst, prc):
        gfbvc.calories = cal
        gfbvc.taste = tst
        gfbvc.price = prc

    def myTaste(asd):#method
        print ("I taste " + asd.taste)

class KoreanFood(Food):
    def __init__ (self, cal, tst, prc, scv):
        Food.__init__(self, cal, tst, prc)
        self.scoville = scv

class FrenchFood(Food):
    def __init__ (self, cal, tst, prc, wne):
        super().__init__(cal, tst, prc,)
        self.wine = wne

    def tastewine(self, vintage):
        print ("This wine tastes " + self.wine + "of " + str(vintage))

f1 = Food(250, "awesome", 30000)
f2 = Food(177, "Gross", 5300)
f3 = KoreanFood(109, "Not Bad", 4000, 300)
f4 = FrenchFood(180, "Fantastic", 30000, "Mutong")

f3.myTaste()
f4.tastewine(1989)

print (f1.calories)
print (f2.calories)

f2.myTaste()
print (f2.price)
