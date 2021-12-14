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

# 54 Spiral Matrix Medium  https://leetcode.com/problems/spiral-matrix/
# Given an m x n matrix, return all elements of the matrix in spiral order.
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        """ Time complexity: O(M * N).
            Space complexity: O(1) if output array isn't considered; O(M * N) otherwise.
        """
        result = list()
        m = len(matrix)
        n = len(matrix[0])
        # count of visited cells
        cell_count = 0

        # index of row that we visit from left to right
        left_to_right_row = 0
        # index of row that we visit from right to left
        right_to_left_row = m - 1
        # index of column that we visit from top to bottom
        top_down_column = n - 1
        # index of column that we visit from bottom to top
        bottom_up_column = 0

        while cell_count < m * n:
            # visit row from left to right
            j = bottom_up_column
            while cell_count < m * n and j < top_down_column + 1:
                result.append(matrix[left_to_right_row][j])
                cell_count += 1
                j += 1
            left_to_right_row += 1
            # visit column from top to bottom
            i = left_to_right_row
            while cell_count < m * n and i < right_to_left_row + 1:
                result.append(matrix[i][top_down_column])
                cell_count += 1
                i += 1
            top_down_column -= 1
            # visit row from right to left
            j = top_down_column
            while cell_count < m * n and j >= bottom_up_column:
                result.append(matrix[right_to_left_row][j])
                cell_count += 1
                j -= 1
            right_to_left_row -= 1
            # visit column from bottom to top
            i = right_to_left_row
            while cell_count < m * n and i >= left_to_right_row:
                result.append(matrix[i][bottom_up_column])
                cell_count += 1
                i -= 1
            bottom_up_column += 1
        return result
