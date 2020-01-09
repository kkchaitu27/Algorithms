#Text copied from www.geeksforgeeks.org

#The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

#1) The subarray which is already sorted.
#2) Remaining subarray which is unsorted.

#In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

def selection_sort_array(array,iteration_index):

     #Recusively call selection_sort_array function till last index
     #Stop criteria for recursion
     if iteration_index == len(array)-1:
          return

     #Initialize minimum value to be at the iteration_index
     minimum_value = array[iteration_index]
     minimum_index = iteration_index
     #Loop from iteration_index till end of array to find minimum value
     for i in range(iteration_index,len(array)):
         if array[i] < minimum_value:
             minimum_index = i
             minimum_value = array[i]

     #Swap minimum value with value at iteration_index
     array[minimum_index] = array[iteration_index]
     array[iteration_index] = minimum_value

     #Sort the array from index iteration_index+1 till last element
     selection_sort_array(array,iteration_index+1)

     #return array
     return array

print(selection_sort_array([5,1,2,9,3,6,1,2],0))
             
