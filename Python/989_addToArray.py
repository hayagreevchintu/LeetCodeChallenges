class Solution:
    def myWhile(self,num):
        if num == 0:
            return 0
        while num > 0:
            yield num % 10
            num = num // 10
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number = 0
        for i in num:
            number = number * 10 + i
        sum_num = number + k
        return [i for i in self.myWhile(sum_num)][::-1] if sum_num != 0 else [0] 