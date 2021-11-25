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

# 27. Remove Element https://leetcode.com/problems/remove-element/
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be
# placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold
# the final result. It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        left_pointer = 0
        for right_pointer in range(len(nums)):
            if nums[right_pointer] != val:
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1
        return left_pointer

    def remove_element_opposite_directions(self, nums: List[int], val: int) -> int:
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        left_pointer = 0
        right_pointer = len(nums)
        while left_pointer < right_pointer:
            if nums[left_pointer] == val:
                nums[left_pointer] = nums[right_pointer - 1]
                right_pointer -= 1
            else:
                left_pointer += 1
        return right_pointer
