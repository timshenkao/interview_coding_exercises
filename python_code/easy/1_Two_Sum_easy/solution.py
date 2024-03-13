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

# 1. Two Sum  https://leetcode.com/problems/two-sum/
# Given an array of integers and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


class Solution:
    def two_sum_brute(self, arr: List[int], target: int) -> List[int]:
        """ Time complexity: O(N ^ 2). We iterate through array in nested loops.
            Space complexity: O(1).
        """
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] + arr[j] == target:
                    return [i, j]

    def two_sum_sorting(self, arr: List[int], target: int) -> List[int]:
        """ Time complexity: O(N * log N). We sort array and iterate through it.
            Space complexity: O(N). We create copy of array and sorting may require O(N) as well.
        """
        left_index = 0
        right_index = len(arr) - 1

        # create copy of array and sort
        # TC: O(N * log N) SC: O(N)
        arr_copy = sorted(arr)
        # TC: O(N) SC: O(1)
        while arr_copy[left_index] + arr_copy[right_index] != target:
            if arr_copy[left_index] + arr_copy[right_index] > target:
                right_index -= 1
            else:
                left_index += 1

        # TC: O(N) SC: O(1)
        result = []
        for i in range(len(arr)):
            if arr[i] == arr_copy[left_index] or arr[i] == arr_copy[right_index]:
                result.append(i)
        return result

    def two_sum_optimal(self, arr: List[int], target: int) -> List[int]:
        """ Time complexity: O(N). We iterate through array.
            Space complexity: O(N). We create lookup dictionary.
        """
        # we keep lookup dictionary of elements that were seen before.
        # Pairs value:index
        lookup = {}
        # iterate through array once
        for i in range(len(arr)):
            # finding key in dictionary is O(1)
            if target - arr[i] in lookup:
                # exercise description says:
                # "You may assume that each input would have exactly one solution"
                # so this code always executes
                return [i, lookup[target - arr[i]]]
            lookup[arr[i]] = i
