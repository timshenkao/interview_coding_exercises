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


# 128. Longest Consecutive Sequence https://leetcode.com/problems/longest-consecutive-sequence/description/
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109


class Solution:
    def longestConsecutive(self, nums):
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        ans = 0
        seen = set(nums)

        for num in nums:
            # `num` is the start of a sequence.
            if num - 1 in seen:
                continue
            length = 0
            while num in seen:
                num += 1
                length += 1
            ans = max(ans, length)
        return ans
