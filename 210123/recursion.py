test_num = 10

def count(num):
    while num>0:
        print(num)
        num -= 1

def count_r(num):
    if num < 1:
        return "끝!"
    print(num)
    return count_r(num-1)

count(test_num)
count_r(test_num)
print(count_r(test_num))
