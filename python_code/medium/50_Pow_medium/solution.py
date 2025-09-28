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

# 50. Pow(x, n)
# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n is an integer.
# Either x is not zero or n > 0.
# -10^4 <= x^n <= 10^4

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """ Time complexity: O(log x). Number of digits in x
            Space complexity: O(1).
        """
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        current_power = x
        while n > 0:
            if n % 2 == 1:
                result *= current_power
            current_power *= current_power
            n //= 2
        return result
