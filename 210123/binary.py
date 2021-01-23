## Divide and Conquer
## 나누어 정복한다.

cit_list = [ 2, 3, 7, 15, 18, 20, 34, 51, 69, 78, 1000] # SORTED

def search(list, num):
    print("Search Start...")
    for elem in list:
        if elem == num:
            return "있음!"
    return "없음.."

def binary_search_recursive(list, start, end, num):
    mid = int (( start + end ) / 2)
    if list[mid] == num:
        print("같다!")
        return "있음!"
    elif list[mid] > num :
        print("작더라!")
        return binary_search_recursive(list, start, mid - 1, num)
    else :
        print("크더라!")
        return binary_search_recursive(list, mid+1, end, num)
    return "없음..."

while True:
    test_num = int ( input("숫자를 입력하세요 : ") )
    print ( binary_search_recursive(cit_list, 0, len(cit_list) -1 ,test_num) )
