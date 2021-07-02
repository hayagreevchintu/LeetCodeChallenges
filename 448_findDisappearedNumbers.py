class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        outputArray = []
        numbersCount = dict.fromkeys(range(1,len(nums)+1),0)
        for i in nums:
            numbersCount[i] += 1
        for i in numbersCount.keys():
            if numbersCount[i] == 0:
                outputArray.append(i)
        return outputArray