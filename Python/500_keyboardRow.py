class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = "qwertyuiop"
        secondRow = "asdfghjkl"
        thirdRow = "zxcvbnm"
        outputArray = words.copy()
        for i in words:
            if i[0].lower() in firstRow:
                for j in range(1, len(i)):
                    if i[j].lower() not in firstRow:
                        outputArray.remove(i)
                        break
            elif i[0].lower() in secondRow:
                for j in range(1, len(i)):
                    if i[j].lower() not in secondRow:
                        outputArray.remove(i)
                        break
            elif i[0].lower() in thirdRow:
                for j in range(1, len(i)):
                    if i[j].lower() not in thirdRow:
                        outputArray.remove(i)
                        break
        return outputArray    