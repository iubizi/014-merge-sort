def process(arr, left, right):
    
    if left == right:
        return
    
    mid = left + int((right-left)>>1)
    process(arr, left, mid)
    process(arr, mid + 1, right)
    merge(arr, left, mid, right)



def merge(arr, left, mid, right):
    
    help_list = [0] * (right-left+1)
    
    i = 0
    left_index = left
    right_index = mid + 1
    
    while left_index <= mid and right_index <= right:
        if arr[left_index] < arr[right_index]:
            help_list[i] = arr[left_index]
            left_index += 1
        else:
            help_list[i] = arr[right_index]
            right_index += 1
        i += 1
    while left_index <= mid:
        help_list[i] = arr[left_index]
        left_index += 1
        i += 1
    while right_index <= right:
        help_list[i] = arr[right_index]
        right_index += 1
        i += 1
        
    for i in range(right-left+1):
        arr[left+i] = help_list[i]



if __name__ == '__main__':
    
    arr = list(range(20))

    import random
    random.shuffle(arr)
    print(arr)

    process(arr, 0, len(arr)-1)
    print(arr)

# [4, 10, 8, 16, 17, 3, 13, 9, 15, 7, 14, 18, 11, 2, 5, 6, 1, 12, 19, 0]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
