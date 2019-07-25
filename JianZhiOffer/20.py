# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self,matrix):
        # write code here
        if not matrix or not matrix[0]:
            return 
        res = []
        while matrix and matrix[0]:
            res += matrix.pop(0)
            
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop(-1)[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res