class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i , j = 0 , len(numbers) - 1

        while i < j:
            delta = target - (numbers[i]+ numbers[j])

            if delta > 0:
                i += 1
            elif delta < 0:
                j -= 1
            else:
                return [i+1, j+1] 