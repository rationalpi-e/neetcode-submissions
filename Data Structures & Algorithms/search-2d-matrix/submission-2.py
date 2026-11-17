class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height , width = len(matrix), len(matrix[0])

        left = 0
        right = height * width -1

        while left <= right:
            mid = (left + right) // 2
            ans = matrix[mid//width][mid % width]
            if target == ans:
                return True
            elif target < ans:
                right = mid -1
            else:
                left = mid + 1

        return False