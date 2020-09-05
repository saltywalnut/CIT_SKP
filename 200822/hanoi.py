def hanoi_moves(num, frombar, midbar, tobar) :
    if num == 1:
        print ("1" + " : " + frombar + " ==>" + tobar)
    else:
        hanoi_moves(num - 1, frombar, tobar, midbar)
        print (str(num) + " : " + frombar + " ==> " + tobar)
        hanoi_moves(num - 1, midbar, frombar, tobar)


plates = 40
barFrom = "A"
barMid = "B"
barTo = "C"
hanoi_moves(plates, barFrom, barMid, barTo)
