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

# 79. Word Search   https://leetcode.com/problems/word-search/
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
# vertically neighboring. The same letter cell may not be used more than once.
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# Could you use search pruning to make your solution faster with a larger board?

VISITED = '+'


class Solution:
    def _backtrack(self, row: int, col: int, board: List[List[str]], suffix: str) -> bool:
        # recursion end case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        m = len(board)
        n = len(board[0])

        # Check the current status, before jumping into backtracking
        if row < 0 or row == m or col < 0 or col == n or board[row][col] != suffix[0]:
            return False

        # mark the choice before exploring further.
        board[row][col] = VISITED
        # explore the 4 neighbor directions
        for row_offset, col_offset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            # word found in the board; no cleanup
            if self._backtrack(row + row_offset, col + col_offset, board, suffix[1:]):
                return True

        # revert the marking
        board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        """ Time complexity: O(m * n * (3 ^ L)). L is the length of the word.
                             There could be m * n invocations of backtracking function in the worst case from exist()
                             function.
                             When backtracking, there is 4 directions initially, but choices are reduced to 3 later
                             (we won't go back to where we come from).
                             Execution trace after the first step could be visualized as a 3-ary tree, each of the
                             branches represent a potential exploration in the corresponding direction.
                             Therefore, in the worst case, the total number of invocation of backtracking function would
                              be the number of nodes in a full 3-nary tree, which is about 3^L.
            Space complexity: O(L).
        """
        m = len(board)
        n = len(board[0])
        for row in range(m):
            for col in range(n):
                if self._backtrack(row, col, board, word):
                    return True
        return False
