// Last updated: 29/11/2025, 16:04:05
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        return (accumulate(nums.begin(), nums.end(), 0) % k);
    }
};