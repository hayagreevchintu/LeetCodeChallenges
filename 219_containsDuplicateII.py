class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictionary = dict()
        for index, val in enumerate(nums):
            if val in dictionary and abs(index - dictionary[val]) <= k:
                return 'true'
            dictionary[val] = index
        return 'false'