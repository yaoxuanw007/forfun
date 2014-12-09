/**
 * https://oj.leetcode.com/problems/find-peak-element/
 */

public class FindPeakElement {
	
	public class Solution {
		public int findPeakElement(int[] num) {
			for (int i = 0; i < num.length; i ++) {
				if ((i == 0 || num[i-1] < num[i]) &&
						(i == num.length - 1 || num[i+1] < num[i]))
					return i;
			}
			return -1;
		}
	}
	
	public static void main(String[] args) {
		FindPeakElement tc = new FindPeakElement();
		Solution s = tc.new Solution();
		int[] num = {1,2,3,1};
		System.out.println(s.findPeakElement(num));
	}
}

