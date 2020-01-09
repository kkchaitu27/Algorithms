/*
 * This algorithm sorts three items which can be represented as 0,1,2
 * This algorithm is of order N(Number Of Items)
 * This algorithm takes at max N swaps
 * 
 */
public class ThreeItemSort {
	
	//Item Array to be sorted
	private int[] itemArray;
	
	public ThreeItemSort(int[] itemArray){
		this.itemArray = itemArray;
	}
	
	//sort Method to sort three items
	public int[] sortThreeItemArray(){
		//Initialize firstItem index to 0 and firstValue to item at zero
		int firstIndex = 0;
		int firstValue = itemArray[0];
		//Initialize thirdIndex as the last item in the array
		int thirdIndex = itemArray.length-1;
		//Initialize seconfValue to zero
		int secondValue = 0;
		//value to iterate till all the first occurences of first Value
		boolean zeroActivated = false;
		
		for(int arrayIndex=1;arrayIndex<itemArray.length;arrayIndex++){
			//Iterate till all are first values
			if(!zeroActivated && firstValue==itemArray[arrayIndex]){
				firstIndex = firstIndex + 1;
				continue;
			} else {
				//Initialize the second value
				secondValue = itemArray[firstIndex+1];
				zeroActivated = true;
			}
			int currentItem = itemArray[arrayIndex];
			//Iterate till all the occurences of second value
			if(currentItem==secondValue) {
				continue;
			}
			//If currentItem is first item, swap first second value with current value
			if(currentItem==firstValue){
				int temp = itemArray[arrayIndex-1];
				itemArray[firstIndex + 1] = firstValue;
				firstIndex++;
				itemArray[arrayIndex] = temp;
				continue;
			}
			//current item is third value, check with thirdIndex item
			if(itemArray[thirdIndex]==currentItem){
				//if arrayIndex is same as thirdIndex, array sorted
				if(arrayIndex==thirdIndex){
					break;
				}
				//Iterate till all the last occurences are of third Item
				while(itemArray[thirdIndex-1]==itemArray[thirdIndex]){
					thirdIndex = thirdIndex - 1;
				}
				thirdIndex = thirdIndex - 1;
				//swapping current item with last non-occurence of third item
				if(itemArray[thirdIndex]==firstValue){
					itemArray[thirdIndex] = currentItem;
					itemArray[firstIndex + 1] = firstValue;
					firstIndex++;
					itemArray[arrayIndex] = secondValue;
				} else if(itemArray[thirdIndex]==secondValue){
					itemArray[thirdIndex] = itemArray[arrayIndex];
					itemArray[arrayIndex] = secondValue;
				} 
			} 
			// Swap thirdIndex if it is equal to firstValue
			else if(itemArray[thirdIndex]==firstValue){
				itemArray[thirdIndex] = itemArray[arrayIndex];
				int temp = secondValue;
				itemArray[firstIndex + 1] = firstValue;
				firstIndex++;
				itemArray[arrayIndex] = temp;
			} 
			//Swap thirdIndex if it is equal to second value
			else if(itemArray[thirdIndex]==secondValue){
				itemArray[thirdIndex] = itemArray[arrayIndex];
				itemArray[arrayIndex] = secondValue;
			}
			//Break the loop if arrayIndex is same as thirdIndex
			if(arrayIndex==thirdIndex){
				break;
			}
		}
		
		return itemArray;
	}
	
	public static void main(String[] args) {
		int[] test = {0,1,2,0,1,2,0,2,0};
		ThreeItemSort object = new ThreeItemSort(test);
		int[] result = object.sortThreeItemArray();
		
		for(int i=0;i<result.length;i++){
			System.out.print(result[i]);
		}
	}

}
