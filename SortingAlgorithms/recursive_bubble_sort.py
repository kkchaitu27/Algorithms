#Text copied from www.geeksforgeeks.org

#Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

def recursive_bubble_sort_array(array,iteration_index):

          #Stop criterion for recursion, iteration from last index to first index
          if iteration_index == 0:
              return

          #Loop through the array pushing largest value to the iteration index
          for i in range(0,iteration_index-1):
              if array[i] > array[i+1]:
                    #Swap adjacent values if the first value is greater than second value
                    value = array[i]
                    array[i] = array[i+1]
                    array[i+1] = value

          #Recursive call sorting the array
          recursive_bubble_sort_array(array,iteration_index-1)
      
          return array

array = [1,9,5,8,2,4,1,3,2,10]
print(recursive_bubble_sort_array(array,len(array)))

