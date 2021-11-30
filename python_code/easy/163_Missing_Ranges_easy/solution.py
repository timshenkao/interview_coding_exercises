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

# 163. Missing Ranges  https://leetcode.com/problems/missing-ranges/
# You are given an inclusive range [lower, upper] and a sorted unique integer array nums,
# where all elements are in the inclusive range.
# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
# Return the smallest sorted list of ranges that cover every missing number exactly.
# That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.
# Each range [a,b] in the list should be output as:
#     "a->b" if a != b
#     "a" if a == b


class Solution:
    def _print_interval(self, lower: int, upper: int) -> str:
        if lower == upper:
            return str(lower)
        else:
            return '->'.join([str(lower), str(upper)])

    def find_missing_ranges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """ Time complexity: O(n). n - number of elements in array
            Space complexity: O(1).
        """
        result = list()
        # empty array
        if not nums:
            result.append(self._print_interval(lower, upper))
            return result

        # handle boundaries
        # if lower bound is less then smallest number in array (not included in array)
        if lower < nums[0]:
            result.append(self._print_interval(lower, nums[0] - 1))

        # handle the very array
        for i in range(len(nums) - 1):
            # if numbers are not consecutive
            if nums[i] != nums[i + 1] - 1:
                result.append(self._print_interval(nums[i] + 1, nums[i + 1] - 1))

        # if upper bound is less then smallest number in array (not included in array)
        if upper > nums[-1]:
            result.append(self._print_interval(nums[-1] + 1, upper))

        return result
