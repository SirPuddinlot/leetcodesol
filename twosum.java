// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int size = nums.length;
        int[] output = new int[2];
        for (int x = 0; x < size - 1; x++){
            for (int n = 0; n < size-1; n++) {
                if (nums[x] + nums[n+1] == target && x != n+1){
                output[0] = x; 
                output[1] = n+1;
                break;
                }
            }
        }
        return output;
    }
}
