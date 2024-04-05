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

# 59. Spiral Matrix II https://leetcode.com/problems/spiral-matrix-ii/description/
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
# 1 <= n <= 20


class Solution:
    def generate_matrix(self, n):
        """ Time complexity: O(N^2).
            Space complexity: O(N^2).
        """
        def direction_to_index(x, y, d):
            if d == "r":
                return (x, y + 1, d) if y + 1 < n and matrix[x][y + 1] == 0 else (x + 1, y, "d")
            elif d == "l":
                return (x, y - 1, d) if y > 0 and matrix[x][y - 1] == 0 else (x - 1, y, "u")
            elif d == "d":
                return (x + 1, y, d) if x + 1 < n and matrix[x + 1][y] == 0 else (x, y - 1, "l")
            else:
                return (x - 1, y, d) if x > 0 and matrix[x - 1][y] == 0 else (x, y + 1, "r")

        matrix = [[0 for i in range(1, n + 1)] for j in range(n)]
        num, direction, i, j = 1, "r", 0, 0
        while 0 <= i < n and 0 <= j < n and matrix[i][j] == 0:
            matrix[i][j] = num
            num += 1
            i, j, direction = direction_to_index(i, j, direction)
        return matrix

    def generate_matrix2(self, n: int) -> List[List[int]]:
        """ Time complexity: O(N^2).
            Space complexity: O(N^2).
        """
        ans = [[0] * n for _ in range(n)]
        count = 1

        for k in range(n // 2):
            j = n - k - 1
            for i in range(k, j):
                ans[k][i] = count
                count += 1
            for i in range(k, j):
                ans[i][j] = count
                count += 1
            for i in range(j, k, -1):
                ans[j][i] = count
                count += 1
            for i in range(j, k, -1):
                ans[i][k] = count
                count += 1

        if n & 1:
            ans[n // 2][n // 2] = count
        return ans
