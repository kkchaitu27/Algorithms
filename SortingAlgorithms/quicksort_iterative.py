#Picking the last element as pivot

def partition(array,low,high):

    i = low - 1

    for j in range(low,high):
        if array[j] <= array[high]:
             i += 1
             value = array[j]
             array[j] = array[i]
             array[i] = value
    value = array[i+1]
    array[i+1] = array[high]
    array[high] = value
    return i+1

def quicksort_iterative(array,low,high):

    size = high - low + 1
    stack = [0]*size

    top = -1
    
    top = top + 1
    stack[top] = low
    top = top+1
    stack[top] = high

    while(top >= 0):
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        pivot = partition(array, low, high)
 
        if pivot-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = pivot - 1

        if pivot+1 < high:
            top = top + 1
            stack[top] = pivot + 1
            top = top + 1
            stack[top] = high



A = [2,5,1,9,3,10,21,32,6,4,7,5]

quicksort_iterative(A,0,len(A)-1)

print(A)
