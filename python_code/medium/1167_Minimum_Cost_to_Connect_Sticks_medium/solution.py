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
from heapq import heapify, heappop, heappush
from typing import List


# 1167. Minimum Cost to Connect Sticks  https://leetcode.com/problems/minimum-cost-to-connect-sticks/
# You have some number of sticks with positive integer lengths.
# These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.
# You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y.
# You must connect all the sticks until there is only one stick remaining.
# Return the minimum cost of connecting all the given sticks into one stick in this way.
# 1 <= sticks.length <= 10 ^ 4
# 1 <= sticks[i] <= 10 ^ 4


class Solution:
    def connect_sticks(self, sticks: List[int]) -> int:
        """ Time complexity: O(n log n). Built-in sorting.
            Space complexity: O(1). We use in-place sort() function.
        """
        # empty array or 1-element array --> nothing to "connect" and cost is zero
        if len(sticks) < 2:
            return 0

        total_cost = 0
        # "convert" array to heap
        heapify(sticks)
        # heap's size decreases by 1 on every iteration
        while len(sticks) > 1:
            # take 2 smallest sticks; heap decreases by 2 elements
            stick1, stick2 = heappop(sticks), heappop(sticks)
            # add them
            curr_cost = stick1 + stick2
            # add current cost to total
            total_cost += curr_cost
            # push current cost back to heap; heap increases by 1 element
            heappush(sticks, curr_cost)
        return total_cost
