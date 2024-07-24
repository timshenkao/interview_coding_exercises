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

# 238. Product of Array Except Self https://leetcode.com/problems/product-of-array-except-self/
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


class Solution:
    def product_except_self(self, nums):
        """ Time complexity: O(N).
            Space complexity: O(N).
        """
        m, res = 1, []
        for i in range(len(nums)):
            res.append(m)
            m *= nums[i]

        m = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= m
            m *= nums[i]
        return res

    def product_except_self2(self, nums: List[int]) -> List[int]:
        """ Time complexity: O(N).
            Space complexity: O(N).
        """
        n = len(nums)
        prefix = [1] * n  # prefix product
        suffix = [1] * n  # suffix product
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in reversed(range(n - 1)):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        return [prefix[i] * suffix[i] for i in range(n)]

    def product_except_self3(self, nums: List[int]) -> List[int]:
        """ Time complexity: O(N).
            Space complexity: O(N).
        """
        n = len(nums)
        ans = [1] * n

        # Use ans as the prefix product array.
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        suffix = 1  # suffix product
        for i, num in reversed(list(enumerate(nums))):
            ans[i] *= suffix
            suffix *= num
        return ans
