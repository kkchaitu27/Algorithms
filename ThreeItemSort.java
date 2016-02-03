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
	
	public int[] sortThreeItemArray(){
		int firstIndex = 0;
		int thirdIndex = itemArray.length-1;
		int firstValue = itemArray[0];
		int secondValue = 0;
		boolean zeroActivated = false;
		
		for(int arrayIndex=1;arrayIndex<itemArray.length;arrayIndex++){
			if(!zeroActivated && firstValue==itemArray[arrayIndex]){
				firstIndex = firstIndex + 1;
				continue;
			} else {
				secondValue = itemArray[firstIndex+1];
				zeroActivated = true;
			}
			int currentItem = itemArray[arrayIndex];
			if(currentItem==secondValue) {
				continue;
			} 
			if(currentItem==firstValue){
				int temp = itemArray[arrayIndex-1];
				itemArray[firstIndex + 1] = firstValue;
				firstIndex++;
				itemArray[arrayIndex] = temp;
				continue;
			}
			if(itemArray[thirdIndex]==currentItem){
				if(arrayIndex==thirdIndex){
					break;
				}
				thirdIndex = thirdIndex - 1;
				if(itemArray[thirdIndex]==firstValue){
					itemArray[thirdIndex] = currentItem;
					itemArray[firstIndex + 1] = firstValue;
					firstIndex++;
					itemArray[arrayIndex] = secondValue;
				} else if(itemArray[thirdIndex]==secondValue){
					itemArray[thirdIndex] = itemArray[arrayIndex];
					itemArray[arrayIndex] = secondValue;
				}
			} else if(itemArray[thirdIndex]==firstValue){
				itemArray[thirdIndex] = itemArray[arrayIndex];
				int temp = secondValue;
				itemArray[firstIndex + 1] = firstValue;
				firstIndex++;
				itemArray[arrayIndex] = temp;
			} else if(itemArray[thirdIndex]==secondValue){
				itemArray[thirdIndex] = itemArray[arrayIndex];
				itemArray[arrayIndex] = secondValue;
			}
			if(arrayIndex==thirdIndex){
				break;
			}
		}
		
		return itemArray;
	}
	
	public static void main(String[] args) {
		int[] test = {2,0,1,1,2,2,2,2,0};
		ThreeItemSort object = new ThreeItemSort(test);
		int[] result = object.sortThreeItemArray();
		
		for(int i=0;i<result.length;i++){
			System.out.print(result[i]);
		}
	}

}
