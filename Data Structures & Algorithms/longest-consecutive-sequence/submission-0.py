class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_long = 0

        for num in nums:
            if (num-1) not in nums:
                curr_num = num
                curr_long = 1
                
                while curr_num + 1 in nums:
                    curr_num += 1
                    curr_long += 1

                max_long = max(max_long, curr_long)

        return max_long