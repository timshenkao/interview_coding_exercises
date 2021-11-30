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

# 268. Missing Number   https://leetcode.com/problems/missing-number/
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that
# is missing from the array.


class Solution:
    def missing_number(self, nums: List[int]) -> int:
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        # actual sum of elements in array
        actual_sum = sum(nums)
        # Gauss formula a_0 = 0, a_n = n and n+1 elements
        theoretical_sum = int(len(nums) * (len(nums) + 1) / 2)
        return theoretical_sum - actual_sum
