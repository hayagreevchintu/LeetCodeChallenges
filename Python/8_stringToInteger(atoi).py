class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        number = 0
        sign = 1
        for i in range(0,len(s)):
            if not s[i].isnumeric():
                if i == 0:
                    if s[i] == '-':
                        sign = -1
                    elif s[i] == '+':
                        sign = 1
                    else:
                        break
                else:
                    break
            elif s[i].isnumeric():
                number = number*10 + int(s[i])
        numberWithSign = number * sign
        if numberWithSign < -2147483648:
            return -2147483648
        elif numberWithSign > 2147483647:
            return 2147483647
        else:
            return numberWithSign