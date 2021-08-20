class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {'{' : '}', '(' : ')', '[' : ']'}
        stack = []
        for i in s:
            if i in "{[(":
                stack.append(i)
            else:
                if stack == []:
                    return False
                test = stack.pop()
                if parantheses[test] != i:
                    return False
        return stack == []