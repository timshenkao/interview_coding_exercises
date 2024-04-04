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

# 228. Summary Ranges  https://leetcode.com/problems/summary-ranges/
# You are given a sorted unique integer array nums.
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such
# that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
#     "a->b" if a != b
#     "a" if a == b


class Solution:
    def _print_range(self, lower: int, upper: int) -> str:
        if lower == upper:
            return str(lower)
        else:
            return "->".join([str(lower), str(upper)])

    def summary_ranges(self, nums: List[int]) -> List[str]:
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        # if array is empty, return empty list
        result = list()

        if len(nums) >= 1:
            left = 0
            for right in range(1, len(nums)):
                # if difference between consecutive elements is greater than 1
                if nums[right] - 1 > nums[right - 1]:
                    # generate and add string
                    result.append(self._print_range(nums[left], nums[right - 1]))
                    left = right
            # handle right boundary, add last element / range
            result.append(self._print_range(nums[left], nums[-1]))
        return result
