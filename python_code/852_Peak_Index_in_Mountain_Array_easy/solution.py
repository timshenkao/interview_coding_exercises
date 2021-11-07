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

# 852. Peak Index in a Mountain Array  https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Let's call an array arr a mountain if the following properties hold:
#  --   arr.length >= 3
#  --   There exists some i with 0 < i < arr.length - 1 such that:
#         arr[0] < arr[1] < ... arr[i-1] < arr[i]
#         arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain, return any i such that
# arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].


class Solution:
    def peak_index_in_mountain_array(self, arr: List[int]) -> int:
        """ Time complexity: O(log N).
            Space complexity: O(1).
        """
        if not arr:
            return -1

        left = 0
        right = len(arr) - 1
        # modification of binary search
        while left <= right:
            middle = left + (right - left) // 2
            if arr[middle - 1] <= arr[middle] >= arr[middle + 1]:
                return middle
            elif arr[middle - 1] <= arr[middle] <= arr[middle + 1]:
                left = middle + 1
            elif arr[middle - 1] >= arr[middle] >= arr[middle + 1]:
                right = middle - 1
