class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n -1

        while left <= right:
            mid_point = (left + right) // 2
            mid_val = matrix[mid_point // n][mid_point % n]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid_point + 1
            else:
                right = mid_point  - 1

        return False