class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        sum_range_nums = 0
        for i in range(len(nums) + 1):
            sum_range_nums += i
        return abs(sum_range_nums - sum_nums)