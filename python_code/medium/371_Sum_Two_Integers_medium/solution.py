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

# 371. Sum of Two Integers  https://leetcode.com/problems/sum-of-two-integers/
#  Given two integers a and b, return the sum of the two integers without using the operators + and -.
# -1000 <= a, b <= 1000


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """ Time complexity: O(1).
                             O(log n), where n is the maximum bit length of the inputs. In the worst case we need up
                             to 32 iterations for a 32-bit integer. Since inputs are in [-1000, 1000], the bit length
                             is at most 11 (since 2^10 = 1024), so effectively O(1) for fixed 32-bit integers.
            Space complexity: O(1).
        """
        # Mask to keep results within 32 bits
        mask = 0xffffffff
        # While there's a carry
        while (b & mask) > 0:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry
        # Handle negative numbers (if high bit is set)
        if (a >> 31) & 1:
            return ~(a ^ mask)
        return a
