// Last updated: 24/11/2025, 17:26:41
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let result = []
    let L = 0
    let R = nums.length-1

    while(L<=R){
        if (Math.abs(nums[L])>Math.abs(nums[R])){
            result.unshift(Math.pow(nums[L], 2))
            L+=1
        } else{
            result.unshift(Math.pow(nums[R], 2))
            R-=1
        }
    }
    return result
};