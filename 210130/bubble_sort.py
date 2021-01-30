test_list = [25,1,34,21,156,3,42,78,41,56]

def bubble_sort(list):
    list_length = len(list)
    end = list_length - 1
    while end >= 1 :
        start = 0
        while start != end :
            print(str(list[start]) + " VS " + str(list[start+1])  )
            if list[start] > list[start+1]:
                print("바꿈!")
                temp = list[start + 1]
                list[start + 1] = list [start]
                list[start] = temp
            print(">>>>>>>>>>")
            start += 1
        print("===========")
        end -= 1
    return list

# [1,25,21,34,3,42,78,41,56,156]
print(bubble_sort(test_list))
