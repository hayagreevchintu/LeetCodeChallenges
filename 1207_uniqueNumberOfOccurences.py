class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict = {}
        sets = set()
        for i in arr:
            if i in dict.keys():
                dict[i] += 1
            else:
                dict[i] = 1
        for i in dict.values():
            sets.add(i)
        return len(sets) == len(dict)