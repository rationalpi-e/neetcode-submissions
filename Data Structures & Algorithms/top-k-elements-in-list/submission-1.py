class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = defaultdict(int)

        for num in nums:
            mydict[num] += 1

        return sorted(mydict.keys() , key= lambda x : mydict[x], reverse = True)[:k]