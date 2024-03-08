class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        my_set=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                my_set.add(matrix[i][j])
        if target in my_set:
            return True
        else:
            return False