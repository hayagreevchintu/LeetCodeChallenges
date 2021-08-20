class Solution(object):
    def longestCommonPrefix(self, strings):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strings) == 0:
            return ""
        current = strings[0]
        for i in range(1,len(strings)):
            temp = ""
            if len(current) == 0:
                break
            for j in range(len(strings[i])):
                if j<len(current) and current[j] == strings[i][j]:
                    temp+=current[j]
                else:
                    break
            current = temp
        return current