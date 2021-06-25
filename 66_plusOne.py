class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in digits:
            number = number * 10 + i
        numberPlusOne = str(number + 1)
        return [i for i in numberPlusOne]