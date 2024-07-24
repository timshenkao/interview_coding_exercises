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

# 36. Valid Sudoku https://leetcode.com/problems/valid-sudoku/description/
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following
# rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """ Time complexity: O(9 * 9) = O(1).
            Space complexity: O(9) = O(1).
            For this specific case, TC and SC are O(1). In general, TC (n^2) and SC O(n)
        """
        # iterate through the sudoku and create a list of all the occupied positions.if 2 positions are the same,
        # return false.
        seen = []
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem != '.':
                    # elem, j and  i, c are in this order to distinguish the row and columns (ex : ('4', 4) and (4,
                    # '4').)
                    seen += [(elem, j), (i, elem), (i//3, j//3, elem)]
        return len(seen) == len(set(seen))
