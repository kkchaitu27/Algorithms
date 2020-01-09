#Text copied from www.geeksforgeeks.org

#Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.


def recursive_insertion_sort(array,iterative_index):
     #Iterate till the last index
     if iterative_index == len(array):
         return
     #Iterate sorted array at the beginning
     for j in range(0,iterative_index):
          #Find whether current element in sorted array is greater than value to be inserted
          if array[j] > array[iterative_index]:
                  #Insert smaller element
                  temp_value = array[j]
                  array[j] = array[iterative_index]
                  array[iterative_index] = temp_value
                  #Copy elements to higher indices
                  for k in range(j+1,iterative_index+1):
                        #Swap the element from current index with ith index till subarray is totall sorted
                        temp_value = array[k]
                        array[k] = array[iterative_index]
                        array[iterative_index] = temp_value
     #Recursively sort the unsorted arrat to the right
     recursive_insertion_sort(array,iterative_index+1)
     return array

array = [1,9,5,8,2,4,1,3,2,10]
print(recursive_insertion_sort(array,0))

