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

# 67. Add Binary  https://leetcode.com/problems/add-binary/
# Given two binary strings a and b, return their sum as a binary string.
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


class Solution:
    def add_binary(self, a: str, b: str) -> str:
        """ Time complexity: O().
            Space complexity: O().
        """
        # constants
        ZERO = "0
        ONE = "1"

        # find out which string is longer
        if len(a) > len(b):
            longer, shorter = a, b
        else:
            longer, shorter = b, a
        longer_pointer, shorter_pointer = len(longer) - 1, len(shorter) - 1

        transfer = 0
        result = list()
        # iterate through longer string and check shorter string as well
        while longer_pointer >= 0:
            if longer[longer_pointer] == ONE:
                transfer += 1
            if shorter_pointer >= 0:
                if shorter[shorter_pointer] == ONE:
                    transfer += 1
                shorter_pointer -= 1

            if transfer % 2 == 1:
                result.append(ONE)
            else:
                result.append(ZERO)
            transfer //= 2
            longer_pointer -= 1

        if transfer == 1:
            result.append(ONE)
        result.reverse()
        return "".join(result)
