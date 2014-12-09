import java.util.HashMap;

/**
 *  https://oj.leetcode.com/problems/two-sum/
 */

public class TwoSum {
	
	public class Solution {
	    public int[] twoSum(int[] numbers, int target) {
	        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
	        int index1 = -1, index2 = -1;
	        for (int i = 0; i < numbers.length; i ++) {
	        	int n = numbers[i], m = target - numbers[i];
	        	if (map.containsKey(Integer.valueOf(m))) {
	        		index1 = map.get(Integer.valueOf(m)).intValue();
	        		index2 = i;
	        		break;
	        	}
	        	map.put(Integer.valueOf(n), Integer.valueOf(i));
	        }
	        return new int[] {index1 + 1, index2 + 1};
	   }
	}
	
	public static void main(String[] args) {
		TwoSum tc = new TwoSum();
		TwoSum.Solution s = tc.new Solution();
		int[] numbers = {2, 7, 11, 15};
		int target = 9;
		int[] result = s.twoSum(numbers, target);
		System.out.println("index1=" + String.valueOf(result[0]) +
				", index2=" + String.valueOf(result[1]));
	}
}

