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

# 152. Maximum Product Subarray https://leetcode.com/problems/maximum-product-subarray/
# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


class Solution:
    def max_product(self, nums: List[int]) -> int:
        """ Time complexity: O(N).
            Space complexity: O(1).
        """
        res, min_pos, max_neg, cur = -float("inf"), float("inf"), -float("inf"), 1
        for num in nums:
            cur *= num
            if cur > res:
                res = cur
            elif 0 < (cur // min_pos) and (cur // min_pos) > res:
                res = cur // min_pos
            elif 0 < (cur // max_neg) and (cur // max_neg) > res:
                res = cur // max_neg

            if cur == 0:
                min_pos, max_neg, cur = float("inf"), -float("inf"), 1
            elif max_neg < cur < 0:
                max_neg = cur
            elif 0 < cur < min_pos:
                min_pos = cur
        return res

    def max_product_optimal(self, nums: List[int]) -> int:
        """ Time complexity: O(N).
            Space complexity: O(1).
        """
        ans = nums[0]
        dp_min = nums[0]  # the minimum so far
        dp_max = nums[0]  # the maximum so far

        for i in range(1, len(nums)):
            num = nums[i]
            prev_min = dp_min
            prev_max = dp_max
            if num < 0:
                dp_min = min(prev_max * num, num)
                dp_max = max(prev_min * num, num)
            else:
                dp_min = min(prev_min * num, num)
                dp_max = max(prev_max * num, num)
            ans = max(ans, dp_max)

        return ans
