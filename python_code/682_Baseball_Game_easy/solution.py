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

# 682. Baseball Game https://leetcode.com/problems/baseball-game/
# You are keeping score for a baseball game with strange rules. The game consists of several rounds,
# where the scores of past rounds may affect future rounds' scores.
# At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i]
# is the ith operation you must apply to the record and is one of the following:
#      An integer x - Record a new score of x.
#      "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two
#      previous scores.
#      "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous
#      score.
#      "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a
#      previous score.
#  Return the sum of all the scores on the record.


# Simple task just to warm up.
# Iterate through list and handle each element.


class Solution:
    def cal_points_brute(self, ops: List[str]) -> int:
        """ Bruteforce approach.
            Time complexity: O(n). We iterate through the whole list once.
            Space complexity: O(n). In the worst case scenario, we add all numbers to temp list.
        """
        temp_list = []
        for i in ops:
            if i == 'C':
                temp_list.pop()
            elif i == 'D':
                temp_list.append(2 * temp_list[-1])
            elif i == '+':
                temp_list.append(temp_list[-1] + temp_list[-2])
            else:
                temp_list.append(int(i))
        return sum(temp_list)
