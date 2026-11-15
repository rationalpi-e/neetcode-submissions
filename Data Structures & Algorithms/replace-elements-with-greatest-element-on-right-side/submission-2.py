class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        max_num = -1

        for i  in range(n-1, -1, -1):
            if res and arr[i+1] > max_num:
                max_num = arr[i+1]
            res.append(max_num)

        return list(reversed(res))