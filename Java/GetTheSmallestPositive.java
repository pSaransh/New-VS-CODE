import java.util.*;
public class GetTheSmallestPositive{
	public static void main(String[] args){
		Integer[] arr = {2,5,6,0,0,1,2};
		int target = 3;
		System.out.println(new GetTheSmallestPositive().mainFun(arr,target));
	}
	public boolean mainFun(Integer[] arr, int target){
		ArrayList<Integer> array = new ArrayList();
		Arrays.sort(arr);
		return Arrays.binarySearch(arr,target)==-1?false:true;
	}
}
