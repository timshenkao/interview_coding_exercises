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

# 7. Reverse Integer https://leetcode.com/problems/reverse-integer/
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        """ Time complexity: O(log x) or O(1) if we consider that x in [-2^31, 2^31 - 1],
                             i.e. no more than 32 (fixed number) iterations
            Space complexity: O(1)
        """
        if x == 0:
            return 0

        # handle negative numbers, remember sign
        sign_flag = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        base = 10
        # every iteration multiply accumulated result by 10 and add digit
        while x:
            result = result * base + x % base
            # specific condition of this exercise
            if result > 2 ** 31:
                return 0
            x //= base
        return sign_flag * result
