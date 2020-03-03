
def countsort(array,exp):

     n = len(array)

     count = [0]*10
     output = [0]*n

     for index,value in enumerate(array):
         quotient = value//exp
         count[quotient%10] += 1


     for i in range(1,10):
         count[i] += count[i-1]

     for i in range(n-1,-1,-1):
         quotient = array[i]//exp
         output[count[quotient%10]-1] = array[i]
         count[quotient%10] -= 1

     for i in range(0,n):
         array[i] = output[i]


def radixsort(array,exp=1):
     
     max_value = max(array)

     while(max_value//exp>0):
         countsort(array,exp)
         exp *= 10

     return array

A = [1,9,2,5,3,10,12,11]

print(radixsort(A))
