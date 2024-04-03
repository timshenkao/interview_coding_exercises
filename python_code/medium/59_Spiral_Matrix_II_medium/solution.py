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

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def dirToIndex(x, y, d):
            if d == "r": return (x, y + 1, d) if y + 1 < n and matrix[x][y + 1] == 0 else (x + 1, y, "d")
            elif d == "d": return (x + 1, y, d) if x + 1 < n and matrix[x + 1][y] == 0 else (x, y - 1, "l")
            elif d == "l": return (x, y - 1, d) if y > 0 and matrix[x][y - 1] == 0 else (x - 1, y, "u")
            else: return (x - 1, y, d) if x > 0 and matrix[x - 1][y] == 0 else (x, y +1, "r")
        matrix = [[0 for i in range(1, n + 1)] for j in range(n)]
        num, dir, i, j = 1, "r", 0, 0
        while 0 <= i < n and 0 <= j < n and matrix[i][j] == 0:
            matrix[i][j] = num
            num += 1
            i, j, dir = dirToIndex(i, j, dir)
        return matrix

    Time: O(n^2)
Space: O(n^2)



class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        count = 1

        for min in range(n // 2):
            max = n - min - 1
            for i in range(min, max):
                ans[min][i] = count
                count += 1
            for i in range(min, max):
                ans[i][max] = count
                count += 1
            for i in range(max, min, -1):
                ans[max][i] = count
                count += 1
            for i in range(max, min, -1):
                ans[i][min] = count
                count += 1

        if n & 1:
            ans[n // 2][n // 2] = count

        return ans