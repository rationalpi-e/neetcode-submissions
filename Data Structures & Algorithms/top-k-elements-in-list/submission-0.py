class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = defaultdict(int)

        for _ in nums:
            mydict[_] += 1

        new = list(sorted(mydict , key= lambda x: mydict[x], reverse=True))

        return new[:k]