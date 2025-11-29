// Last updated: 29/11/2025, 16:24:31
1class Solution {
2public:
3    int minOperations(vector<int>& nums, int k) {
4        int sum = accumulate(nums.begin(), nums.end(), 0);
5        return (sum % k);
6    }
7};