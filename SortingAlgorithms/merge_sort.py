#Text copied from www.geeksforgeeks.org

#Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

#MergeSort(arr[], l,  r)
#If r > l
#     1. Find the middle point to divide the array into two halves:  
#             middle m = (l+r)/2
#     2. Call mergeSort for first half:   
#             Call mergeSort(arr, l, m)
#     3. Call mergeSort for second half:
#             Call mergeSort(arr, m+1, r)
#     4. Merge the two halves sorted in step 2 and 3:
#             Call merge(arr, l, m, r)

def merge(left,right):
      #Final sorted array to be constructed
      array = []
      #Whether final sorted array constructed or not
      sorted_array = False
      #Left array pointer
      left_index = 0
      #Right array pointer
      right_index = 0
      #Loop till the final sorted array is formed
      while(not sorted_array):
             #Check whetherleft pointed element is less than right pointed element
             if left_index < len(left) and right_index < len(right) and left[left_index] < right[right_index]:
                   #Add element to the array
                   array += [left[left_index]]
                   left_index += 1
             elif right_index < len(right):
                   #Add element from right array
                   array += [right[right_index]]
                   right_index += 1
             elif left_index < len(left):
                   #Add element from left array
                   array += [left[left_index]]
                   left_index += 1
             else:
                   pass
             if left_index == len(left) and right_index == len(right):
                    sorted_array = True
      return array



def merge_sort(array, left_index, right_index):
    
      if right_index > left_index:
               middle = int((left_index + right_index)/2)
               left_sorted = merge_sort(array,left_index,middle)
               right_sorted = merge_sort(array,middle+1,right_index)
               sorted_array = merge(left_sorted,right_sorted)
      elif right_index == left_index:
               sorted_array = [array[left_index]]
      else:
               pass

      return sorted_array

array = [1,9,5,8,2,4,1,3,2,10]
print(merge_sort(array,0,len(array)-1))

