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

# 118. Pascal's Triangle  https://leetcode.com/problems/pascals-triangle/
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        """ Time complexity: O(n ^ 2). There are 2 nested loops and each loop requires O(n).
            Space complexity: O(n ^ 2). We create output list and current row list. Current row list has O(n) elements.
                              Output list contains all currents rw list's.
        """
        result = list()
        # empty triangle
        if num_rows == 0:
            pass
        # add the first row
        if num_rows >= 1:
            result.append([1])
        # populate and add other rows
        if num_rows > 1:
            for i in range(1, num_rows):
                # first element in a row is always 1
                curr_row = [1]
                # this loop actually runs for rows 3, 4, ...
                # these rows in Python have indices 2, 3, 4, ...
                for j in range(1, i):
                    curr_row.append(result[i - 1][j - 1] + result[i - 1][j])
                # last element in a row is always 1
                curr_row.append(1)
                result.append(curr_row)
        return result


