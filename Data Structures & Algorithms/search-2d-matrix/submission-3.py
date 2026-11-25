class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return  False
            
        length , width = len(matrix) ,  len(matrix[0])
        left, right = 0 , length * width - 1

        while left <= right:
            mid =  (left + right) // 2
            ans = matrix[mid // width][mid % width]
            if ans == target:
                return True
            elif ans < target:
                left = mid + 1
            else:
                right = mid - 1 

        return False