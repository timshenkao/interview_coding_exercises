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

# 704. Binary Search https://leetcode.com/problems/binary-search/
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search
# target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search_recursion(self, nums: List[int], target: int) -> int:
        """ Time complexity: O(log N).
            Space complexity: O(1). If we count Python recursion stack, then O(log N)
        """
        def _search(left, right):
            if left > right:
                return -1
            middle = left + (right - left + 1) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return _search(middle + 1, right)
            elif nums[middle] > target:
                return _search(left, middle - 1)
            else:
                return -1

        if not nums:
            return -1
        return _search(0, len(nums) - 1)

    def search_iteration(self, nums: List[int], target: int) -> int:
        """ Time complexity: O(log N).
            Space complexity: O(1).
        """
        left_index = 0
        right_index = len(nums) - 1
        while left_index <= right_index:
            middle = left_index + (right_index - left_index) // 2
            if nums[middle] == target:
                return middle
            if target < nums[middle]:
                right_index = middle - 1
            else:
                left_index = middle + 1
        return -1

    def search_iteration2(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        left, right = 0, n - 1
        if nums[left] == target:
            return 0
        if nums[left] > target or nums[right] < target:
            return -1

        # midpoint is always strictly between left and right
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            return right
        return -1
