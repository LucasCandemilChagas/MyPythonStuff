
# Time Complexity is O(n^2) in the best, 
# average, and worst cases
def selection_sort(list):
    n = len(list)
    for i in range(n-1):
        
        # The better thing to do is always assume that
        # the current minimum value is the first element
        # in the list
        min_indx = i
        
        # Now iterate through the unsorted portion 
        # of the list
        for j in range(i+1,n):
            
            # If list[min_indx] is smaller than list[j], 
            # then it continues to be the smallest one
            # if not then the value of min_indx will be j
            if list[j] < list[min_indx]:
                min_indx = j

        # Swap the found minimum element with the first element
        # in the unsorted portion of the list
        if min_indx != i:
            list[i], list[min_indx] = list[min_indx], list[i]
        
arr = [64,25,12,22,11]
print(arr)

selection_sort(arr)

print(arr)

# Simplest algorithm
#Time Complexity of O(n^2)
def bubble_sort(arr):
    n = len(arr)
    
    #Traverse the list
    for i in range(n):  
        swapped = False
        
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped in inner loop,
        # then the list is sorted
        if swapped == False:
            break

arr = [64,25,12,22,11]

print('Bubble')
print(arr)

bubble_sort(arr)

print(arr)


# Best case: O(n) when the list is sorted
# Average and Worst case: O(n^2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
print('Insertion')
print(arr)

insertion_sort(arr)

print(arr)

# Time Complexity is O(nlogn)
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    
    L = [0] * n1
    R = [0] * n2
    
    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        # Find the mid index Ex: len = 10, mid = 4 
        mid = (left + right) // 2
        
        # Takes the left portion to divide
        merge_sort(arr,left, mid)
        
        # Takes the right portion to divide
        merge_sort(arr,mid+1,right)
        
        
        merge(arr,left,mid,right)

print('Merge')
print(arr)

merge_sort(arr, 0, len(arr) - 1)

print(arr)




