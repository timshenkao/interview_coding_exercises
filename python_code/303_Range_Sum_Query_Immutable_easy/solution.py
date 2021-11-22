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

# 303. Range Sum Query - Immutable  https://leetcode.com/problems/range-sum-query-immutable/
# Given an integer array nums, handle multiple queries of the following type:
#     Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.


class NumArray:

    def __init__(self, nums: List[int]):
        self.cumul_sum = [0]
        # pre-compute the cumulative sum from index 0 to k.
        for i in range(len(nums)):
            self.cumul_sum.append(self.cumul_sum[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        """ Time complexity: O(1) time per query, O(n) time pre-computation.
                             Since the cumulative sum is cached, each sumRange query can be calculated in O(1) time.
            Space complexity: O(n).
        """
        return self.cumul_sum[right + 1] - self.cumul_sum[left]
