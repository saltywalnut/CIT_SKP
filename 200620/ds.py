a = [5, "bill", "bob", True, 7]
print (a)
print (a[0]+a[3])
a[0] = 0
print (a)
a[4] = a[4] + a[0]

b = {"age" : 24, "name" : "Elsa", "isMarried": False}
print (b)
print (b["age"])
b["isMarried"] = True
print(b)

moon = {"lastname" : "Moon", "isMarried" : True, "Nationality" : "SK"}
kim = {"lastname" : "Kim", "isMarried" : True, "Nationality" : "NK"}
trump = {"lastname" : "trump", "isMarried" : False, "Nationality" : "USA"}

canmarryKimMoon = (not moon["isMarried"]) and (not kim ["isMarried"])

print(canmarryKimMoon)
