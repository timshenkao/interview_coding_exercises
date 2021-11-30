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

# 415. Add Strings  https://leetcode.com/problems/add-strings/
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
# You must also not convert the inputs to integers directly.


class Solution:
    def add_strings(self, num1: str, num2: str) -> str:
        """ Time complexity: O(n) where n - length of the longest string
            Space complexity: O(n). We create list to keep output result.
        """
        result = list()
        base = 10

        # define which string is longer
        if len(num1) > len(num2):
            longest, shortest = num1, num2
        else:
            longest, shortest = num2, num1

        shortest_pointer = len(shortest) - 1
        longest_pointer = len(longest) - 1
        transfer = 0
        # iterate through the longest string
        while longest_pointer >= 0:
            if shortest_pointer >= 0:
                transfer, digit = divmod(int(longest[longest_pointer]) + int(shortest[shortest_pointer]) + transfer,
                                         base)
                shortest_pointer -= 1
            else:
                # the shortest string is over, we have unhandled digits in the largest string
                transfer, digit = divmod(int(longest[longest_pointer]) + transfer, base)
            result.append(str(digit))
            longest_pointer -= 1
        # there could be unhandled transfer when the first digit in the largest string is 9
        if transfer:
            result.append('1')

        return ''.join([result[i] for i in reversed(range(len(result)))])
