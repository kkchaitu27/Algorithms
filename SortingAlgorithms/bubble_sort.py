#Text copied from www.geeksforgeeks.org

#Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

def bubble_sort_array(array):
      
      #Whether array is sorted or not
      done = False

      #Loop till the array is sorted
      while(not done):
          #Check to see if swapping of elements occured, if there is no swap, array is sorted.
          swap = False
          #Loop through the array doing swaps of elements
          for i in range(0,len(array)-1):
              if array[i] > array[i+1]:
                    value = array[i]
                    array[i] = array[i+1]
                    array[i+1] = value
                    swap = True
          if not swap:
              done = True

      return array

print(bubble_sort_array([1,9,5,8,2,4,1,3,2,10]))
