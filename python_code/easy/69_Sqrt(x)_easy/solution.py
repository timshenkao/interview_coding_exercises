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


# 69. Sqrt(x)  https://leetcode.com/problems/sqrtx/
# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result
# is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.


class Solution:
    def my_sqrt(self, x: int) -> int:
        """ Time complexity: O(log x).
                The search space is reduced by half each iteration. Since x can be up to 2^31 - 1, the maximum
                number of iterations is log2(x).
            Space complexity: O(1).
        """
        # 0 and 1
        if x < 2:
            return x

        # use modification of binary search
        low = 0
        high = x
        while low <= high:
            middle = low + (high - low) // 2
            square = middle * middle
            if square == x:
                return middle
            elif square < x:
                low = middle + 1
            else:
                high = middle - 1
        return high
