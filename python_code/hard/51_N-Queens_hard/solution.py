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

# 51. N-Queens  https://leetcode.com/problems/n-queens/
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each
# other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate
# a queen and an empty space, respectively.
# 1 <= n <= 9


class Solution:
    def solve_n_queens(self, n):
        """ Time complexity: O(n * n!).
            Space complexity: O(n * n!).
        """
        def dfs(i, l, r, m, arr):
            if i == n:
                res.append(arr)
            else:
                l = l[1:] + [0]
                r = [0] + r[:-1]
                for j in range(n):
                    if m[j] == l[j] == r[j] == 0:
                        l[j] = r[j] = m[j] = 1
                        dfs(i + 1, l, r, m, arr + [("." * j) + "Q" + ("." * (n - j - 1))])
                        l[j] = r[j] = m[j] = 0
        res = []
        dfs(0, [0] * n, [0] * n, [0] * n, [])
        return res

    def solve_n_queens2(self, n):
        """ Time complexity: O(n * n!).
            Space complexity: O(n * n!).
        """
        def dfs(i, board):
            if i == n:
                ans.append(board)
                return
            for j in range(n):
                if cols[j] or diag1[i + j] or diag2[j - i + n - 1]:
                    continue
                cols[j] = diag1[i + j] = diag2[j - i + n - 1] = True
                dfs(i + 1, board + ['.' * j + 'Q' + '.' * (n - j - 1)])
                cols[j] = diag1[i + j] = diag2[j - i + n - 1] = False

        ans = []
        cols = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)
        dfs(0, [])
        return ans
