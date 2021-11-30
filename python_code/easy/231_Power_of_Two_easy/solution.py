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

# 231. Power of Two https://leetcode.com/problems/power-of-two/
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2 ^ x.


class Solution:
    def is_power_of_two(self, n: int) -> bool:
        """ Time complexity: O(1). n is 32-bit integer.
            Space complexity: O(1).
            000000001    1
            000000010    2
            000000100    4
            000001000    8
            000010000    16
            000100000    16
            001000000    64
        """
        if n == 0:
            return False
        return log2(n).is_integer()

    def is_power_of_two_bitmask(self, n: int) -> bool:
        """ Time complexity: O(1). n is 32-bit integer.
            Space complexity: O(1).
            000000001    1
            000000010    2
            000000100    4
            000001000    8
            000010000    16
            000100000    16
            001000000    64
        """
        if n == 0:
            return False
        # check power of 2
        check_power_two = n & (n-1) == 0
        return check_power_two
