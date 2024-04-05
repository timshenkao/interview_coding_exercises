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
import bisect

# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given
# target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9


class Solution(object):
    def search_range(self, nums, target):
        l, r = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1
        return [l, r] if 0 <= l <= r else [-1, -1]

    def search_range2(self, nums: List[int], target: int) -> List[int]:
        """ Time complexity: O(log N). Binary Search
            Space complexity: O(1).
        """
        left = bisect.bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target) - 1
        return [left, right]
