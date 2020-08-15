mode = 0
m = [
{"id" : "12345", "balance" : 50000, "name" : "name1"},
{"id" : "11111", "balance" : 1000, "name" : "name2"},
{"id" : "22222", "balance" : 2000, "name" : "name3"},
{"id" : "33333", "balance" : 7000, "name" : "name4"},
{"id" : "44444", "balance" : 500, "name" : "name5"},
]
members = 5

inputnum =  input ("Enter your 5 digit card number: ")

user = "user undefined"


count = 0
while count < members :
    if(m[count]["id"] == inputnum):
        user = m[count]
    count += 1

print ("Welcome, " + user["name"] + " you have $" + str(user["balance"]) + " in your bank account")

def fun ():
    mode = int (input ("To withdraw, press 1. To deposit, press 2. To finish, press 3: "))
    if mode == 1:
        wdcash = int(input ( "How much would you like to withdraw?") )
        if wdcash > user["balance"]:
            print ("Please withdraw within your balance.")
            mode == 1
        else:
            user["balance"] -= wdcash
            print (user["balance"])
            fun()

    if mode == 2:
        dpcash =  int ( input("How much would you like to deposit?"))
        user["balance"] += dpcash
        print (user["balance"])
        fun()

    if mode == 3:
        print ("Goodbye.")

fun()
