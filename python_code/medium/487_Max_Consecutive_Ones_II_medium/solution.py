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

# 487. Max Consecutive Ones II https://leetcode.com/problems/max-consecutive-ones-ii/
# Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.
# 1 <= nums.length <= 10 ^ 5
# nums[i] is either 0 or 1.
# What if the input numbers come in one by one as an infinite stream?
# In other words, you can't store all numbers coming from the stream as it's too large to hold in memory.
# Could you solve it efficiently?


class Solution:
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        """ Time complexity: O(N). Fast and slow pointers.
            Space complexity: O(1).
        """
        slow_pointer, fast_pointer = 0, 0
        longest_sequence = 0
        zeroes_seen = 0
        # we use 2 pointers: fast and slow
        while fast_pointer < len(nums):
            if nums[fast_pointer] == 0:    # add the right most element into our window
                zeroes_seen += 1

            # we have seen 2 zeroes, either consecutive or not
            # move slow pointer further
            while zeroes_seen == 2:
                if nums[slow_pointer] == 0:
                    zeroes_seen -= 1
                slow_pointer += 1

            # update longest sequence
            longest_sequence = max(longest_sequence, fast_pointer - slow_pointer + 1)
            fast_pointer += 1
        return longest_sequence
