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

# 509. Fibonacci Number https://leetcode.com/problems/fibonacci-number/
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is
# the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).


class Solution:
    # there are other interesting "mathematical" approaches: Matrix Exponentiation (Fibonacci sequence in matrix form)
    # and "golden ratio". But there time complexity and space complexity are not straightforward to estimate.
    # "Golden ratio" gives approximate value when n is large.
    # https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

    def fibonacci_recursion(self, n: int) -> int:
        """ Time complexity: O(2 ^ n). Recurrence relation: T(n) = T(n-1) + T(n-2) which gives exponential time.
            Space complexity: O(n). Recursion stack requires O(n)
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci_recursion(n - 1) + self.fibonacci_recursion(n - 2)

    def fibonacci_iteration(self, n: int) -> int:
        """ Time complexity: O(N). We iterate from 0 to n-1
            Space complexity: O(1).
        """
        if n <= 1:
            return n

        # iterate from 0 to n
        prev_prev = 0
        prev = 1
        i = 1
        while i < n:
            temp = prev_prev + prev
            prev_prev = prev
            prev = temp
            i += 1
        return prev
