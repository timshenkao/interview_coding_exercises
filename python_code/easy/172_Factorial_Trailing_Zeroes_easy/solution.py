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


# 172. Factorial Trailing Zeroes   https://leetcode.com/problems/factorial-trailing-zeroes/
# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.


class Solution:
    def trailing_zeroes(self, n: int) -> int:
        """ Time complexity: O(n log n) or O(n) amortized
            Space complexity: O(1).
        """
        if 5 > n:
            return 0

        result = 0
        for i in range(5, n + 1, 5):
            power_of_5 = 5
            while i % power_of_5 == 0:
                result += 1
                power_of_5 *= 5
        return result

    def trailing_zeroes_optimal(self, n: int) -> int:
        """ Time complexity: O(log n). There are (log_5 n) of 5 less-than-or-equal-to n.
                             Because the multiplications and divisions are within the 32-bit integer range,
                             we treat these calculations as O(1), i.e. log_5 n * O(1) = log n operations
            Space complexity: O(1).
        """
        if 5 > n:
            return 0

        result = 0
        while n:
            n //= 5
            result += n
        return result
