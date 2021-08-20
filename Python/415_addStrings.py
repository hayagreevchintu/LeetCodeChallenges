class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        int_num1 = 0
        int_num2 = 0
        for i in num1:
            int_num1 = int_num1 * 10 + (ord(i) - ord('0'))
        for i in num2:
            int_num2 = int_num2 * 10 + (ord(i) - ord('0'))
        return str(int_num1 + int_num2)