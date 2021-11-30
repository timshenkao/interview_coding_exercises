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

# 463. Island Perimeter  https://leetcode.com/problems/island-perimeter/
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and
#  grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.


class Solution:
    def island_perimeter(self, grid: List[List[int]]) -> int:
        """ Time complexity: O(nm). n - number of rows, m - number of columns
            Space complexity: O(1).
        """
        perimeter = 0
        num_rows = len(grid)
        num_columns = len(grid[0])
        # iterate row-by-row
        for row in range(num_rows):
            # iterate column-by-column within row
            for col in range(num_columns):
                # current cell's perimeter
                curr_cell_perimeter = 0
                # if cell is "land", we should consider its borders and calculate perimeter per the cell
                if grid[row][col] == 1:
                    # if current cell is on the left border, increase its perimeter
                    if col == 0:
                        curr_cell_perimeter += 1
                    else:
                        # otherwise, if cell to the left is "water", increase current cell's perimeter
                        if grid[row][col - 1] == 0:
                            curr_cell_perimeter += 1
                    # if current cell is on the right border, increase its perimeter
                    if col == (num_columns - 1):
                        curr_cell_perimeter += 1
                    else:
                        # otherwise, if cell to the right is "water", increase current cell's perimeter
                        if grid[row][col + 1] == 0:
                            curr_cell_perimeter += 1
                    # if current cell is on the top border, increase its perimeter
                    if row == 0:
                        curr_cell_perimeter += 1
                    else:
                        # otherwise, if cell to the top is "water", increase current cell's perimeter
                        if grid[row - 1][col] == 0:
                            curr_cell_perimeter += 1

                    # if current cell is on the bottom border, increase its perimeter
                    if row == (num_rows - 1):
                        curr_cell_perimeter += 1
                    else:
                        # otherwise, if cell to the bottom is "water", increase current cell's perimeter
                        if grid[row + 1][col] == 0:
                            curr_cell_perimeter += 1
                perimeter += curr_cell_perimeter
        return perimeter

    def island_perimeter_optimized(self, grid: List[List[int]]) -> int:
        """ Time complexity: O(nm). n - number of rows, m - number of columns
            Space complexity: O(1).
        """
        perimeter = 0
        num_rows = len(grid)
        num_columns = len(grid[0])

        # iterate row-by-row
        for row in range(num_rows):
            # iterate column-by-column within row
            for col in range(num_columns):
                # if cell is "land", it may have maximum perimeter 4
                if grid[row][col] == 1:
                    perimeter += 4
                    # if current cell is not on the top border and cell to the top is "land",
                    # decrease current cell's perimeter by 1 and top cell's perimeter by 1
                    if row > 0 and grid[row - 1][col] == 1:
                        perimeter -= 2
                    # if current cell is not on the left border and cell to the left is "land",
                    # decrease current cell's perimeter by 1 and right cell's perimeter by 1
                    if col > 0 and grid[row][col - 1] == 1:
                        perimeter -= 2
        return perimeter
