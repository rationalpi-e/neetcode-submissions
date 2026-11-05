class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = defaultdict(int)

        for i in range(len(nums)):
            need = target - nums[i]

            if need in mydict:
                return [mydict[need], i]

            mydict[nums[i]] = i
