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

# 53. Maximum Subarray  https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
# and return its sum.
# A subarray is a contiguous part of an array.


class Solution:
    def max_sub_array_kadane(self, nums: List[int]) -> int:
        """ Time complexity: O(). Kadane's algorithm: it's a variant of dynamic programming.
            Space complexity: O().
        """
        # empty array
        if not nums:
            return 0

        # Initialize our variables using the first element.
        current_value = max_value = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            current_value = max(num, current_value + num)
            max_value = max(max_value, current_value)

        return max_value
