def selection_sort(arr):
    for i in range(len(arr)):
        minV = arr[i]
        index = i
        for j in range(i+1,len(arr)):
            if (arr[j]<minV):
                minV = arr[j]
                index = j
        arr[i],arr[index] = arr[index], arr[i]


def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i-j] < arr[i-j-1]:
                arr[i-j],arr[i-j-1] = arr[i-j-1],arr[i-j]
            else:
                break
    return arr
        
def bubble_sort(arr):
    flag = True
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = False
        if flag:
            return
        else:
            flag = True



def quick_sort(arr):
    left_sub_arr = []
    right_sub_arr = []
    if len(arr) <= 1:   
        return arr
    pivot = arr[-1]
    for i in range(len(arr)-1):
        if arr[i]<pivot:
            left_sub_arr.append(arr[i])
        else:
            right_sub_arr.append(arr[i])
    return quick_sort(left_sub_arr)+[pivot]+quick_sort(right_sub_arr)


# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     middle = len(arr)//2
#     left_sub_arr = merge_sort(arr[:middle])
#     right_sub_arr = merge_sort(arr[middle:])
#     result = []
#     while(True):
#         if len(left_sub_arr) == 0:
#             result += right_sub_arr
#             break
#         elif len(right_sub_arr) == 0:
#             result += left_sub_arr
#             break
#         elif left_sub_arr[0] < right_sub_arr[0]:
#             result.append(left_sub_arr.pop(0))
#         else:
#             result.append(right_sub_arr.pop(0))
#     return result



#below code will still work but difference is that it modifies the
#given array but the above code returns new array without changing the 
#given array.

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    middle = len(arr)//2
    left_sub_arr = merge_sort(arr[:middle])
    right_sub_arr = merge_sort(arr[middle:])
    arr.clear()
    while(True):
        if len(left_sub_arr) == 0:
            arr += right_sub_arr
            break
        elif len(right_sub_arr) == 0:
            arr += left_sub_arr
            break
        elif left_sub_arr[0] < right_sub_arr[0]:
            arr.append(left_sub_arr.pop(0))
        else:
            arr.append(right_sub_arr.pop(0))
    return arr





array = [742,56,34,7,32,34,745,34,2,434,12,203]
arr2 = [742,56,34,7,32,34,745,34,2,434,12,203]
arr3 = [12,9]

# print(array)

# print(insertion_sort(array))
# bubble_sort(arr2)
# insertion_sort(arr3)
# insertion_sort(arr2)
# # insertion_sort(arr3)

# print(array)
merge_sort(arr2)
print(arr2)
# print(arr3)
# print(quick_sort(arr2))
