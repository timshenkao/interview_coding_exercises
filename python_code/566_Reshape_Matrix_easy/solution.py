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

# 566. Reshape the Matrix  https://leetcode.com/problems/reshape-the-matrix/
# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a
# different size r x c keeping its original data.
# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number
# of columns of the wanted reshaped matrix.
# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order
# as they were.
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix;
# Otherwise, output the original matrix.


class Solution:
    def matrix_reshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """ Time complexity: O(m * n). We iterate through each element via 2 nested loops
            Space complexity: O(m * n). We create result (reshaped) matrix
        """
        orig_r = len(mat)
        orig_c = len(mat[0])
        # check if reshape is impossible
        if r * c != orig_r * orig_c:
            return mat

        result = [[0 for _ in range(c)] for _ in range(r)]
        mat_i = mat_j = 0
        for row in range(r):
            for col in range(c):
                result[row][col] = mat[mat_i][mat_j]
                # we achieved last column in original matrix; go to the next row
                if mat_j == orig_c - 1:
                    mat_i += 1
                    mat_j = 0
                else:
                    mat_j += 1
        return result
