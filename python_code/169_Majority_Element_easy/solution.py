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

# 169. Majority Element https://leetcode.com/problems/majority-element/
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        """ Time complexity: O(n).
            Space complexity: O(1).
            Boyer-Moore Voting Algorithm. It works as
                    majority_element_occurrences - minority_element_occurrences >= 1
        """
        curr_count = 0
        possible_majority_element = None

        for elem in nums:
            # either we've just started handling the array or previous elements "crossed out" each other
            if curr_count == 0:
                possible_majority_element = elem
            # at some iteration (even the last one), counter will become positive and never get back to zero.
            if elem == possible_majority_element:
                curr_count += 1
            else:
                curr_count -= 1
        return possible_majority_element
