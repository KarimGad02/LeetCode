class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums){
        vector<string> result;
        if (nums.empty()) return result;
        if (nums.size() == 1){
            result.push_back(to_string(nums[0]));
            return result;
        }
        int left = 0;
        int right = 1;
        int control = 1;
        while (right < nums.size()) {
            if (nums[left] + control != nums[right]) {
                if (control == 1)
                    result.push_back(to_string(nums[left]));
                else
                    result.push_back(to_string(nums[left]) + "->" + to_string(nums[right - 1]));

                left = right;
                control = 0;
            }
            control++;
            right++;
        }
        if (control == 1)
            result.push_back(to_string(nums[left]));
        else
            result.push_back(to_string(nums[left]) + "->" + to_string(nums[right - 1]));
        return result;
    }
};