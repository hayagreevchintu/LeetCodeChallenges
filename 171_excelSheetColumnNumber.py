class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnNumbers = dict()
        result = 0
        alphabetTeller = range(65,91)
        for i in alphabetTeller:
            columnNumbers[chr(i)] = i - 64
        for i in columnTitle:
            result = result*26 + columnNumbers[i]
        return result