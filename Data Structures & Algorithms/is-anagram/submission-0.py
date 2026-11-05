class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict = defaultdict(int)

        for _ in s:
            mydict[_] += 1

        for _ in t:
            mydict[_] -= 1

        for i in mydict.values():
            if i != 0:
                return False
        return True