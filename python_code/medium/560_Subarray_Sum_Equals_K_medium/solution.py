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
import collections

# 560. Subarray Sum Equals K https://leetcode.com/problems/subarray-sum-equals-k/
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7


class Solution:
    def subarray_sum(self, nums, k):
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        sums, res, sm = {}, 0, 0
        for i in range(len(nums)):
            sums[sm], sm = sm in sums and sums[sm] + 1 or 1, sm + nums[i]
            if sm - k in sums:
                res += sums[sm - k]
        return res

    def subarray_sum2(self, nums: List[int], k: int) -> int:
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        ans = 0
        prefix = 0
        count = collections.Counter({0: 1})
        for num in nums:
            prefix += num
            ans += count[prefix - k]
            count[prefix] += 1
        return ans
