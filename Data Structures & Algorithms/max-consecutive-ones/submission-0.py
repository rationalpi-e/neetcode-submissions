class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        curr_streak = 0

        for num in nums:
            if num != 1:
                curr_streak = 0
            else:
                curr_streak += 1

            max_streak = max(max_streak , curr_streak)

        return max_streak