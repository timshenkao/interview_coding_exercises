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

# 1004. Max Consecutive Ones III https://leetcode.com/problems/max-consecutive-ones-iii/
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array
# if you can flip at most k 0's.
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length


class Solution:
    def longest_ones(self, nums: List[int], k: int) -> int:
        # enumerate() returns iterator
        # Time complexity: O(n) as we iterate
        # Space complexity: O(n) as we create additional list
        zeros, res = [-1] + [i for i, c in enumerate(nums) if not c] + [len(nums)], 0
        for j in range(k + 1, len(zeros)):
            res = max(res, zeros[j] - zeros[j - k - 1] - 1)
        return res or k and len(nums)

    def longest_ones_optimal(self, nums: List[int], k: int) -> int:
        # Time complexity: O(n)
        # Space complexity: O(1)
        # enumerate() returns iterator
        ans = 0
        left = 0
        # sliding window with left and right pointers
        # right pointer moves on and window expands
        for right, num in enumerate(nums):
            if num == 0:
                k -= 1
            # shrink window, move left pointer to the right
            while k < 0:
                # if we meet 0, then "unflip" it
                if nums[left] == 0:
                    k += 1
                left += 1
            # update answer with current window size
            ans = max(ans, right - left + 1)
        return ans
