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
    def exist(self, board: List[List[str]], word: str) -> bool:
        """ Time complexity: O().
            Space complexity: O().
        """
        m = len(board)
        n = len(board[0])
        curr_i = curr_j = 0
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    curr_i, curr_j = i, j
                    board[i][j] = VISITED
                    break

        print(curr_i, curr_j)
        if curr_i == 0 and curr_j == 0 and board[curr_i][curr_j] != word[0]:
            return False

        for ch in word[1:]:
            if (0 <= curr_i - 1 < m) and (0 <= curr_j < n) and board[curr_i - 1][curr_j] == ch:
                board[curr_i - 1][curr_j] = VISITED
                curr_i -= 1
            elif (0 <= curr_i + 1 < m) and (0 <= curr_j < n) and board[curr_i + 1][curr_j] == ch:
                board[curr_i + 1][curr_j] = VISITED
                curr_i += 1
            elif (0 <= curr_i < m) and (0 <= curr_j - 1 < n) and board[curr_i][curr_j - 1] == ch:
                board[curr_i][curr_j - 1] = VISITED
                curr_j -= 1
            elif (0 <= curr_i < m) and (0 <= curr_j + 1 < n) and board[curr_i][curr_j + 1] == ch:
                board[curr_i][curr_j + 1] = VISITED
                curr_j += 1
            else:
                return False
        return True
