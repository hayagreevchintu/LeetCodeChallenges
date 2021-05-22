class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while True:
            try:
                if nums[i] == val:
                    nums.remove(nums[i])
                else:
                    i += 1
            except:
                break
        return len(nums)