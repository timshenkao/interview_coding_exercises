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


# 191. Number of 1 Bits  https://leetcode.com/problems/number-of-1-bits/
# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the
# Hamming weight).
# Note:
#     Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be
#     given as a signed integer type. It should not affect your implementation, as the integer's internal binary
#     representation is the same, whether it is signed or unsigned.
#     In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3,
#     the input represents the signed integer. -3.


class Solution:
    def hamming_weight(self, n: int) -> int:
        """ Time complexity: O(1). n is a 32-bit integer, number of iterations is upper bounded.
            Space complexity: O(1).
        """
        # checks if the rightmost bit is 1
        bitmask = 1
        # used as a "flag" whether there are still bits to handle
        remnant = n
        count = 0
        # iterate if there is at least one bit set to 1
        # remnant is updated on each iteration
        while remnant:
            if bitmask & remnant:
                count += 1
            # update "flag", remove rightmost bit / shift right
            remnant = remnant >> 1
        return count

    def hamming_weight_flip_last(self, n: int) -> int:
        """ Time complexity: O(1). n is a 32-bit integer, number of iterations is upper bounded.
            Space complexity: O(1).
        """
        count = 0
        remnant = n
        # iterate if there is at least one bit set to 1
        while remnant:
            count += 1
            # update "flag", flip rightmost 1-bit
            # AND
            # Brian Kernighan's Algorithm (Bit Trick)
            remnant &= (remnant - 1)
        return count
