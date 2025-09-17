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

# 283. Move Zeros https://leetcode.com/problems/move-zeroes/
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the
# non-zero elements.
# Note that you must do this in-place without making a copy of the array.


class Solution:
    def move_zeros(self, arr: List[int]) -> None:
        """ Time complexity: O(n). We iterate through the list
            Space complexity: O(1).
        """
        # "pointer" to the current first zero element
        first_zero_index = -1
        # number of zeros seen - 1
        skipped_consecutive_zeros = 0

        for i in range(len(arr)):
            # we already saw zero element
            if first_zero_index > -1:
                # another zero element, just increase counter of skipped zeros
                if arr[i] == 0:
                    skipped_consecutive_zeros += 1
                # "exchange" current non-zero element with current zero element
                else:
                    arr[first_zero_index], arr[i] = arr[i], 0
                    first_zero_index = first_zero_index + 1
                    # first_zero_index = i - skipped_consecutive_zeros
            # we haven't seen zero element yet
            elif arr[i] == 0:
                first_zero_index = i

    def move_zeros_subtle(self, arr: List[int]) -> None:
        """ Time complexity: O(n). We iterate through the list
            Space complexity: O(1).
        """
        # despite simplicity, it's very subtle solution
        # we don't need to keep track of number of skipped consecutive zeroes
        # we have 2 pointers; they point to the same element initially
        # if there is no zeroes yet, pointers continue to point to the same element on each iteration
        # if there was zero, left pointer points to the first zero element; right goes on
        # iteration
        l = 0
        for r in range(len(arr)):
            if arr[r]:
                arr[l], arr[r] = arr[r], arr[l]
                l +=1
