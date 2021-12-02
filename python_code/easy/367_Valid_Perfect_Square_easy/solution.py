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

# 367. Valid Perfect Square  https://leetcode.com/problems/valid-perfect-square/
# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.
# 1 <= num <= 2^31 - 1

class Solution:
    def _my_sqrt(self, n: int) -> bool:
        """ Time complexity: O(log n).
            Space complexity: O(1).
        """
        # 0 and 1
        if n < 2:
            return True

        # use modification of binary search
        low = 0
        high = n
        while low <= high:
            middle = low + (high - low) // 2
            if middle * middle == n:
                return True
            elif middle * middle < n:
                low = middle + 1
            else:
                high = middle - 1
        return False

    def is_perfect_square(self, num: int) -> bool:
        """ Time complexity: O(log n)
            Space complexity: O(1)
        """
        return self._my_sqrt(num)

    def is_perfect_square_newton(self, num: int) -> bool:
        """ Time complexity: O(log n)  because guess sequence converges quadratically
                             https://arnold.hosted.uark.edu/NA/Pages/OrderConv.pdf
            Space complexity: O(1)
        """
        # 0 and 1
        if num < 2:
            return True

        # Newton's method
        temp = num // 2
        while temp * temp > num:
            temp = (temp + num // temp) // 2
        return temp * temp == num
