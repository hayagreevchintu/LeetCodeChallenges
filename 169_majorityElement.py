class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_count = {}
        for i in nums:
            if i in nums_count.keys():
                nums_count[i] += 1
            else:
                nums_count[i] = 1
        for i in nums:
            if nums_count[i] >= ceil(len(nums)/2):
                return i
        