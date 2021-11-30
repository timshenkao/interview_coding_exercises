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

# 561. Array Partition I  https://leetcode.com/problems/array-partition-i/
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
# such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.


class Solution:
    def array_pair_sum(self, nums: List[int]) -> int:
        """ Time complexity: O(N log N). Python's built-in sorting is O(N log N)
            Space complexity: O(1).  List's method sort() is in-place.
                              If sorted() is used, then O(n) as it creates and returns new list.
        """
        # sort the array and sum integers at odd places
        # pairs' indexes are of the kind (2 * i, 2 * i + 1), i = 0, 1, 2, ...
        nums.sort()
        accum = 0
        for i in range(0, len(nums), 2):
            accum += nums[i]
        return accum
