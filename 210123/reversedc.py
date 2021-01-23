## Divide and Conquer
## 나누어 정복한다.

cit_list_r = [ 78, 51, 40, 33, 21, 10, 8, 7, 3, 1] # SORTED_Reversed
cit_list = [ 2, 3, 7, 15, 18, 20, 34, 51, 69, 78] # SORTED

def search(list, num):
    print("Search Start...")
    for elem in list:
        if elem == num:
            return "있음!"
    return "없음.."

def binary_search(list, num):
    list_size = len(list)
    idx_start = 0
    idx_end = list_size - 1
    while idx_start <= idx_end:
        idx_middle = int (( idx_start + idx_end ) / 2)
        if list[idx_middle] == num:
            print("같다!")
            return "있음!"
        elif list[idx_middle] > num :
            print("작더라!")
            idx_start = idx_middle + 1
        else :
            print("크더라!")
            idx_end = idx_middle - 1

    return "없음..."

while True:
    test_num = int ( input("숫자를 입력하세요 : ") )
    print ( binary_search(cit_list_r, test_num) )
