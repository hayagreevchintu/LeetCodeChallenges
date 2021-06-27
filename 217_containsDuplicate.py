class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        else:
            nums_count = {}
            for i in nums:
                if i in nums_count.keys():
                    return True
                else:
                    nums_count[i] = 1
            return False