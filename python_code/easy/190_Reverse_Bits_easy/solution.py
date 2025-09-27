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

# 190. Reverse Bits  https://leetcode.com/problems/reverse-bits/
# Reverse bits of a given 32 bits unsigned integer.


class Solution:
    def reverse_bits(self, n: int) -> int:
        """ Time complexity: O(1). n is 32-bit integer.
            Space complexity: O(1).
        """
        if not n:
            return 0

        n_size = 32
        remnant = n
        bitmask = 1
        zero_counter = 0
        result = 0
        for i in range(1, n_size + 1):
            # count leading zeros to append to the end
            if not remnant:
                zero_counter += 1
            else:
                # rightmost bit is 1
                if remnant & bitmask:
                    if zero_counter:
                        result = result << zero_counter
                        zero_counter = 0
                    result = result << 1
                    result |= 1
                else:
                    zero_counter += 1
                remnant = remnant >> 1
        # append leading zeros to the end
        if zero_counter:
            result = result << zero_counter
        return result

    def reverse_bits_shorter(self, n: int) -> int:
        """ Time complexity: O(1). n is 32-bit integer.
            Space complexity: O(1).
        """
        result = 0
        # 32 bit integer: powers of 2 from 0 to 31
        power = 31
        while n:
            # apply mask and shift rightmost bit to the left "power" times and add to result
            result += (n & 1) << power
            n = n >> 1
            power -= 1
        return result
