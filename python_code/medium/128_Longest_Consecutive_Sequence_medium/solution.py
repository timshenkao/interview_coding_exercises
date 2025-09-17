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
        # we can't sort array as O(n) is required
        ans = 0
        seen = set(nums)

        for num in nums:
            # check if `num` is the start of a sequence.
            # Since each number is only checked once as part of its sequence, and hash set operations
            # are O(1) on average, the total time is O(n).
            if num - 1 in seen:
                # skip current element as it's not start of a sequence
                # it is either already handled or would be handled as a part of some sequence
                continue
            # no previous integer in lookup set, i.e. current element is the start of new sequence
            length = 0
            # Count consecutive numbers
            # tricky moment: we iterate through set (not original array)
            # but such iteration happens for start of sequence only
            while num in seen:
                num += 1
                length += 1
            ans = max(ans, length)
        return ans
