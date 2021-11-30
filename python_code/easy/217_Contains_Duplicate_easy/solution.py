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

# 217. Contains Duplicate  https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
# element is distinct.


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        # if there is less than 2 elements, then there is no duplicates
        if len(nums) < 2:
            return False

        # keep dictionary as a counter
        table = dict()
        for elem in nums:
            _ = table.setdefault(elem, 0)
            table[elem] += 1
            # return immediately
            if table[elem] > 1:
                return True
        return False

    def contains_duplicate_sorting(self, nums: List[int]) -> bool:
        """ Time complexity: O(n log n).
            Space complexity: O(1) if sorting is in-place.
                              O(n) if sorting is NOT in-place.
        """
        # if there is less than 2 elements, then there is no duplicates
        if len(nums) < 2:
            return False
        # built-in method sort() is in-place
        nums.sort()
        for i in range(len(nums) - 1):
            # compare 2 consecutive elements
            if nums[i] == nums[i + 1]:
                return True
        return False
