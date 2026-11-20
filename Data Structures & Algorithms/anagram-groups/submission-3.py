class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)

        for s in strs:
            mydict[''.join(sorted(s))].append(s)

        return list(mydict.values())