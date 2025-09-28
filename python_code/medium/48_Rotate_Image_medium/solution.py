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

# 48. Rotate Image https://leetcode.com/problems/rotate-image/
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """ Time complexity: O(N ^ 2). We move each element at once.
                             Matrix rotation by 90 degrees (clockwise) is actually combination of 2 operations:
                             transpose and reflect.
            Space complexity: O(1).
        """
        def rotate(matrix: list[list[int]]) -> None:
            n = len(matrix)

            # Transpose the matrix (swap elements across the main diagonal)
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            # Reverse each row
            for i in range(n):
                matrix[i].reverse()

        def rotate_cyclic(self, matrix: List[List[int]]) -> None:
            """ Time complexity: O(N ^ 2). We move each element at once. Exchange / rotate groups of
                                    4 elements directly
                Space complexity: O(1).
            """
            # columns and rows are from 0 to (n-1) in Python
            n = len(matrix) - 1

            # if matrix dimension is odd, then include "central" row
            if len(matrix) % 2 == 1:
                num_rows = len(matrix) // 2 + 1
            # if matrix dimension is even, then include half of rows
            else:
                num_rows = len(matrix) // 2

            # include half of columns
            num_cols = len(matrix) // 2

            for i in range(num_rows):
                for j in range(num_cols):
                    matrix[j][n - i], matrix[n - i][n - j], matrix[n - j][i], matrix[i][j] \
                        = matrix[i][j], matrix[j][n - i], matrix[n - i][n - j], matrix[n - j][i]
