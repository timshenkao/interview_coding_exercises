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

from math import log2, floor

# 476. Number Complement  https://leetcode.com/problems/number-complement/
# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in
# its binary representation.
#     For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.


class Solution:
    def find_complement(self, num: int) -> int:
        """ Time complexity: O(1).
            Space complexity: O(1)
        """
        # construct full bitmask
        bitmask = num
        # propagate 1-bits from leftmost positions to the rightmost via right shift and use OR
        bitmask |= (bitmask >> 1)
        bitmask |= (bitmask >> 2)
        bitmask |= (bitmask >> 4)
        bitmask |= (bitmask >> 8)
        bitmask |= (bitmask >> 16)
        # flip all bits
        return bitmask ^ num

    def find_complement_bit_by_bit(self, num: int) -> int:
        """ Time complexity: O(1).
            Space complexity: O(1)
        """
        bitmask = 1
        # used as a "flag" whether there are still bits to handle
        remnant = num
        # iterate if there is at least one bit set to 1
        # bitmask is updated on each iteration
        while remnant:
            # flip current bit
            num = num ^ bitmask
            # shift bitmask left to handle the next bit on next iteration
            bitmask = bitmask << 1
            # update "flag", remove rightmost bit
            remnant = remnant >> 1
        return num

    def find_complement_full_mask(self, num: int) -> int:
        """ Time complexity: O(1).
            Space complexity: O(1)
        """
        # n is a length of num in binary representation
        n = floor(log2(num)) + 1
        # bitmask has the same length as num and contains only ones 1...1
        bitmask = (1 << n) - 1
        # flip all bits
        return bitmask ^ num
