class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        if len(s)!=0:
            return len(str(s[len(s)-1]))
        return 0