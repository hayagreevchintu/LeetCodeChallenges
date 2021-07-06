class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        length = len(nums) - 1
        while i <= length:
            a = nums.pop(i)
            if a in nums:
                nums.remove(a)
            else:
                return a