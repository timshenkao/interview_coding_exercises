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

# 697. Degree of an Array  https://leetcode.com/problems/degree-of-an-array/
# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency
# of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums
# that has the same degree as nums.


class Solution:
    def find_shortest_subarray(self, nums: List[int]) -> int:
        """ Time complexity: O(N). We iterate through array once and then handle map
            Space complexity: O(N). We create map of "statistics" per number
        """
        # map of the kind:
        #   key: number from array nums
        #   value: list of 3 values [count of number appearances, index of the first appearance,
        #          index of the last appearance]
        elems = dict()
        for i in range(len(nums)):
            elem = elems.get(nums[i], [])
            if not elem:
                elems[nums[i]] = [1, i, i]
            else:
                elems[nums[i]][0] += 1
                elems[nums[i]][2] = i

        # iterate through the populated map and find element with:
        #       a) maximum count and
        #       b) minimum distance if counts are the same
        # initialize with the first number from array for simplicity
        max_count = elems[nums[0]][0]
        min_distance = elems[nums[0]][2] - elems[nums[0]][1] + 1
        for k, v in elems.items():
            if (v[0] > max_count) or (v[0] == max_count and (v[2] - v[1] + 1) < min_distance):
                max_count = v[0]
                min_distance = v[2] - v[1] + 1

        return min_distance
