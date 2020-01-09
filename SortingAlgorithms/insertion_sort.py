#Text copied from www.geeksforgeeks.org

#Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.


def insertion_sort(array):
     #Iterate till the last index
     for i in range(0,len(array)):
          #Iterate sorted array at the beginning
          for j in range(0,i):
              #Find whether current element in sorted array is greater than value to be inserted
              if array[j] > array[i]:
                  #Insert smaller element
                  temp_value = array[j]
                  array[j] = array[i]
                  array[i] = temp_value
                  #Copy elements to higher indices
                  for k in range(j+1,i+1):
                        #Swap the element from current index with ith index till subarray is totall sorted
                        temp_value = array[k]
                        array[k] = array[i]
                        array[i] = temp_value
     return array

array = [1,9,5,8,2,4,1,3,2,10]
print(insertion_sort(array))
