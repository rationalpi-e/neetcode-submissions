class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)

        for _ in strs:
            mydict[''.join(sorted(_))].append(_)

        return  list(mydict.values())