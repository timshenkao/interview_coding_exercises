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

# 167. Two Sum II - Input Array Is Sorted   https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of
# length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.


class Solution:
    def two_sum(self, arr: List[int], target: int) -> List[int]:
        """ Time complexity: O(N).
            Space complexity: O(1).
        """
        left_index = 0
        right_index = len(arr) - 1
        # iterate through array once
        while left_index < right_index:
            if arr[left_index] + arr[right_index] == target:
                return [left_index + 1, right_index + 1]
            elif arr[left_index] + arr[right_index] > target:
                right_index -= 1
            elif arr[left_index] + arr[right_index] < target:
                left_index += 1
        return []
