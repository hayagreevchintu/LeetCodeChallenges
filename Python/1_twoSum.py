class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_sample = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dict_sample.keys():
                return [dict_sample[target-nums[i]],i]
            else:
                dict_sample[nums[i]] = i