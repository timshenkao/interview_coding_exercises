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

from typing import List

# 73. Set Matrix Zeroes  https://leetcode.com/problems/set-matrix-zeroes/
# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
# You must do it in place.
# A straightforward solution using O(mn) space is probably a bad idea. A simple improvement uses O(m + n) space, but
# still not the best solution. Could you devise a constant space solution?
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2 ^ 31 <= matrix[i][j] <= 2 ^ 31 - 1


class Solution:
    def set_zeroes(self, matrix: List[List[int]]) -> None:
        """ Time complexity: O(m * n).
            Space complexity: O(1).
        """
        m = len(matrix)
        n = len(matrix[0])
        # separate flag to see if there is zero in the first row
        first_row_zero = False
        # separate flag to see if there is zero in the first column
        first_column_zero = False

        # Check if first row has any zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if first column has any zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_column_zero = True
                break

        # Use first row and column as markers for zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # set zeros besides first row and first column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        # set zeros in the first row if necessary
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        # set zeros in the first column if necessary
        if first_column_zero:
            for i in range(m):
                matrix[i][0] = 0
