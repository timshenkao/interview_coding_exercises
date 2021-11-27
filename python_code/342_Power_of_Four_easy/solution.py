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

from math import log2

# 342. Power of Four  https://leetcode.com/problems/power-of-four/
# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n = 4 ^ x.


class Solution:
    def is_power_of_four(self, n: int) -> bool:
        """ Time complexity: O(1). n is 32-bit integer.
            Space complexity: O(1).
            000000001    1
            000000100    4
            000010000    16
            001000000    64
            100000000    256
            log_4 n = 1/2 * log_2 n So, log_2 n should be even
        """
        if n == 0:
            return False
        return log2(n) % 2 == 0

    def is_power_of_four_bitmask(self, n: int) -> bool:
        """ Time complexity: O(1). n is 32-bit integer.
            Space complexity: O(1).
            000000001    1
            000000100    4
            000010000    16
            001000000    64
            100000000    256
            32-bit representation of mask: 10101010101010101010101010101010
            hexadecimal representation of mask: 0xaaaaaaaa
        """
        bitmask = 0xaaaaaaaa
        if n == 0:
            return False
        # check power of 2
        check_power_two = n & (n-1) == 0
        # check bitmask
        check_bitmask = n & bitmask == 0
        return check_power_two and check_bitmask

    def is_power_of_four_modulo(self, n: int) -> bool:
        """ Time complexity: O(1). n is 32-bit integer.
            Space complexity: O(1).
            000000001    1
            000000100    4
            000010000    16
            001000000    64
            100000000    256
            4 ^ k mod 3)=(3+1) ^ k mod 3 = 1
            If x is a power of two and x % 3 == 1, then x is a power of four.
        """
        if n == 0:
            return False
        # check power of 2
        check_power_two = n & (n-1) == 0
        # check modulo
        check_modulo = n % 3 == 1
        return check_power_two and check_modulo
