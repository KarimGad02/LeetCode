// Last updated: 29/11/2025, 16:21:29
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        return (sum % k);
    }
};