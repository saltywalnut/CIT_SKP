# number = 1
# division = 1
# while division < number:
#     number + 1
#     if number % division > 0:
#         division + 1



n = 2

while n < 1000:
    divider = 2
    count = 0

    while divider < n:
        if n%divider == 0:
            count = count + 1
        divider = divider + 1

    if count == 0:
        print (n)

    n = n + 1
