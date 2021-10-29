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

# 977. Squares of a Sorted Array  https://leetcode.com/problems/squares-of-a-sorted-array/
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
# non-decreasing order.


class Solution:
    def sorted_squares_brute(self, arr: List[int]) -> List[int]:
        """ Time complexity: O(n * log n). We use built-in Python sorting algorithm (TimSort).
            Space complexity: Usually TimSort requires O(1) but in the worst case it is O(n).
        """
        for i in range(len(arr)):
            arr[i] *= arr[i]
        return sorted(arr)

    def sorted_squares(self, arr: List[int]) -> List[int]:
        """ Time complexity: O(n). We iterate through list once.
            Space complexity: O(n). We use additional list to keep sorted integers
        """
        # we have 2 pointers:
        # left pointer goes from left to right to handle possible negative integers
        # right pointer goes from right to left to handle possible non-negative integers
        left_index = 0
        right_index = len(arr) - 1

        # initialize output list
        result = [0] * len(arr)
        i = len(arr) - 1
        while left_index <= right_index:
            # if there is negative integer
            if abs(arr[left_index]) > abs(arr[right_index]):
                result[i] = arr[left_index] * arr[left_index]
                left_index += 1
            # if there is negative integer
            else:
                result[i] = arr[right_index] * arr[right_index]
                right_index -= 1
            i -= 1
        return result
