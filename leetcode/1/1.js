/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let numsMap = {};
    for(let i = 0; i<nums.length; i++){
        complement = target - nums[i];
        if (complement in numsMap){
            return [numsMap[complement], i]
        }
        numsMap[nums[i]] = i
    }
    return [];
};

console.log(twoSum([2, 7, 11, 15], 9)); 