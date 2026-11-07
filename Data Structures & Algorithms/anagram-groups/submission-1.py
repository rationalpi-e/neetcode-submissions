class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)

        for word in strs:
            mydict[''.join(sorted(word))].append(word)

        return list(mydict.values())