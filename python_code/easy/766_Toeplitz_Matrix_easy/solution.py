# Copyright (c) 2021 - present, Timur Shenkao
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################

# 766. Toeplitz Matrix https://leetcode.com/problems/toeplitz-matrix/
# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 20
# 0 <= matrix[i][j] <= 99
# What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the
# matrix into the memory at once?
# What if the matrix is so large that you can only load up a partial row into the memory at once?


class Solution:
    def is_toeplitz_matrix(self, matrix):
        """ Time complexity: O(mn).
            Space complexity: O(1).
        """
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

    def is_toeplitz_matrix2(self, matrix):
        """ Time complexity: O(mn).
            Space complexity: O(1).
        """
        return all(matrix[i][j] == matrix[i - 1][j - 1]
                   for i in range(1, len(matrix)) for j in range(1, len(matrix[0])))

    def is_toeplitz_matrix_follow1(self, matrix):
        """ Time complexity: O(mn).
            Space complexity: O(n).
        """
        if not matrix or not matrix[0]:
            return True

        m = len(matrix)
        n = len(matrix[0])
        buffer = matrix[0]
        for i in range(1,m):
            for j in range(n - 1):
                if (buffer[j] != matrix[i][j + 1]):
                    return False
            buffer = matrix[i]
        return True
