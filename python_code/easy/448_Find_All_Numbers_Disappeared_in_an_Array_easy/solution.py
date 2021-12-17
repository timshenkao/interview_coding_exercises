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

# 448. Find All Numbers Disappeared in an Array  https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Given an array of n integers where integer is in the range [1, n], return an array of all the integers in
# the range [1, n] that do not appear in array.


class Solution:
    def find_disappeared_numbers_brute(self, arr: List[int]) -> List[int]:
        """ Time complexity: O(n).
            Space complexity: O(n). We need space for set of all integers in [1, n]
        """
        # the advantage of this solution is that the original array is not altered

        # time O(n) to create set
        # space O(n) to keep set
        correct_set = set(range(1, len(arr) + 1))

        # time O(n) to create set
        # space O(n) to keep set
        given_set = set(arr)

        return list(correct_set - given_set)

    def find_disappeared_numbers_optimal(self, arr: List[int]) -> List[int]:
        """ Time complexity: O(n). We iterate through the whole array twice
            Space complexity: O(n). We need to generate and keep output list
        """
        # the idea is not to sort the array but to mark positions in the original array
        # by inverting the sign (multiplying by -1) or adding some number > n
        mark = len(arr) + 1  # mark can be any integer greater n

        for i in range(len(arr)):
            # Take integer and use it as index
            # Subtract / remove mark first
            if arr[i] >= mark:
                new_index = arr[i] - 1 - mark
            else:
                new_index = arr[i] - 1
            # mark position at new_index if we have not visited it yet
            if arr[new_index] < mark:
                arr[new_index] += mark

        missing_nums = []

        # Iterate over positions  from 1 to n and add all those
        # unmarked integers to the output array
        for i in range(len(arr)):
            if arr[i] < mark:
                missing_nums.append(i + 1)
        return missing_nums
