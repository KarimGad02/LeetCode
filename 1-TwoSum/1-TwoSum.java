// Last updated: 29/11/2025, 16:26:48
1class Solution {
2    public int[] twoSum(int[] nums, int target) {
3        int[] result = new int[2];
4        outerloop:
5        for(int i = 0; i < nums.length; i++){
6            for(int j = 0; j < nums.length; j++){
7                if(nums[i] + nums[j] == target && i != j){
8                    result[0]=i;
9                    result[1]=j;
10                    break outerloop;
11                }
12            }
13        }
14        return result;
15    }
16}