#Heap Sort Algorithm for sorting in increasing order:
#1. Build a max heap from the input data.
#2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of tree.
#3. Repeat above steps while size of heap is greater than 1.

#Heapify the array
def heapify(array,n,i):
   largest = i
   left = 2*i + 1
   right = 2*i + 2
   #Check Left child if it is larger
   if left < n and array[largest] < array[left]:
        largest = left
   #Check right child  if it is larger     
   if right < n and array[largest] < array[right]:
        largest = right
   #If left or right child is larger,swap and heapify again
   if largest != i:
        array[i],array[largest] = array[largest],array[i]

        heapify(array,n,largest)

#Main function to heapify and swap elements to sort the array
def heapsort(array):

   n = len(array)

   for i in range(n,-1,-1):
       heapify(array,n,i)

   for i in range(n-1,0,-1):
       array[i],array[0] = array[0],array[i]
       heapify(array,i,0)


A = [5,1,3,8,9,10,12,3]

heapsort(A)

print(A)
