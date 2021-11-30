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


# 504. Base 7  https://leetcode.com/problems/base-7/
# Given an integer num, return a string of its base 7 representation.


class Solution:
    def convert_to_base7(self, num: int) -> str:
        """ Time complexity: O(n) where n - number of digits
            Space complexity: O(n). We create list of calculated digits in base 7
        """
        if num == 0:
            return '0'

        result = []
        transfer = 0
        base = 7

        # handle negative numbers
        sign = num < 0
        num = abs(num)

        while num:
            num, last_digit = divmod(num, base)
            if last_digit + transfer > base - 1:
                result.append(str(last_digit - base + transfer))
                transfer = 1
            else:
                result.append(str(last_digit + transfer))
                transfer = 0
        # if there is transfer unhandled in previous loop
        if transfer:
            result.append(str(1))
        # append negative sign
        if sign:
            result.append('-')
        return ''.join([result[i] for i in reversed(range(len(result)))])
