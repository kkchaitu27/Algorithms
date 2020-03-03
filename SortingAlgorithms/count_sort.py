

def count_sort(array):

    n = len(array)
    max_value = max(array)
    min_value = min(array)
    value_range = max_value - min_value + 1
    count = [0]*value_range

    for i in range(0,n):
         count[array[i]-min_value] +=1

    for i in range(1,len(count)):
         count[i] += count[i-1]

    print(count)

    output = [0]*n
    for i in range(n-1,-1,-1):
       output[count[array[i]-min_value] -1] = array[i]
       count[array[i]-min_value] -= 1

    for i in range(0,n):
       array[i] = output[i]

    return array


A = [1,7,10,2,3,9,4]

print(count_sort(A))
       


