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

# 202. Happy Number  https://leetcode.com/problems/happy-number/
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not
#     include 1.
#     Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


class Solution:
    def _calculate_next(self, n):
        total = 0
        while n > 0:
            n, last_digit = divmod(n, 10)
            total += last_digit * last_digit
        return total

    def is_happy(self, n: int) -> bool:
        """ Time complexity: O(log n).
            Space complexity: O(log n).
                                  3 possibilities for a number:
                                    a) It eventually gets to 1.
                                    b) It eventually gets stuck in a cycle. Keep set or dict to track elements.
                                    c) It keeps going higher and higher, up towards infinity.  NEVER HAPPENS
        """
        previous = set()
        while n != 1 and n not in previous:
            previous.add(n)
            n = self._calculate_next(n)
        return n == 1

    def is_happy_precalc(self, n: int) -> bool:
        """ Time complexity: O(log n).
            Space complexity: O(1).
                                  3 possibilities for a number:
                                    a) It eventually gets to 1.
                                    b) It eventually gets stuck in a cycle.
                                       There's only one cycle: 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 44. All other
                                       numbers are on chains that lead into this cycle, or on chains that lead into 1.
                                    c) It keeps going higher and higher, up towards infinity.  NEVER HAPPENS
        """
        common_cycle = {4, 16, 37, 58, 89, 145, 42, 20}
        while n != 1 and n not in common_cycle:
            n = self._calculate_next(n)
        return n == 1
