class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCounter = {}
        magazineCounter = {}
        for i in ransomNote:
            if i in ransomNoteCounter.keys():
                ransomNoteCounter[i] += 1
            else:
                ransomNoteCounter[i] = 1
        for i in magazine:
            if i in magazineCounter.keys():
                magazineCounter[i] += 1
            else:
                magazineCounter[i] = 1
        for i in ransomNote:
            try:
                if magazineCounter[i] >= ransomNoteCounter[i]:
                    continue
                else:
                    return False
            except:
                return False
        return True