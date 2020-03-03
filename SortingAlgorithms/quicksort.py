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


def quicksort(array,low,high):
     if (low < high):
         pi = partition(array, low, high)

         quicksort(array,low,pi-1)
         quicksort(array,pi+1,high)


A = [2,5,1,9,3,10,21,32,6,4,7,5]

quicksort(A,0,len(A)-1)

print(A)
