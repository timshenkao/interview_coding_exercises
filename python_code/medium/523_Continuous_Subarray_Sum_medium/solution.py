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

# 523. Continuous Subarray Sum https://leetcode.com/problems/continuous-subarray-sum/
# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
# A good subarray is a subarray where:
#       its length is at least two, and
#       the sum of the elements of the subarray is a multiple of k.
# Note that:
#       A subarray is a contiguous part of the array.
#       An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= sum(nums[i]) <= 2^31 - 1
# 1 <= k <= 2^31 - 1


class Solution:
    def check_subarray_sum(self, nums: List[int], k: int) -> bool:
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        prefix = 0
        prefix_to_index = {0: -1}

        for i, num in enumerate(nums):
            prefix += num
            if k != 0:
                prefix %= k
            if prefix in prefix_to_index:
                if i - prefix_to_index[prefix] > 1:
                    return True
            else:
                # Set a new key if it's absent because the previous index is better.
                prefix_to_index[prefix] = i
        return False
