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


# 12. Integer to Roman  https://leetcode.com/problems/integer-to-roman/
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together.
# 12 is written as XII, which is simply X + II.
# The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the
# five we subtract it making four. The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.
# 1 <= num <= 3999

BASE = 10


class Solution:
    def int_to_roman(self, num: int) -> str:
        """ Time complexity: O(1). Upper limit for number is 3999 by condition, it is Roman number MMMCMXCIX.
                             The longest Roman number is MMMDCCCLXXXVIII (3888).
                             Outer loop may have 4 iterations at most. There could 15 iterations total
                             (including inner iterations)
            Space complexity: O(1). The longest number is MMMDCCCLXXXVIII
        """
        correspondence = {1: ['I', 'V', 'X'], 2: ['X', 'L', 'C'], 3: ['C', 'D', 'M'], 4: ['M']}

        total_result = list()
        iteration = 0
        while num:
            # storage for Roman representation of current digit
            temp_result = list()
            # number of decimal order
            iteration += 1
            roman_digits = correspondence[iteration]
            num, digit = divmod(num, BASE)
            if digit == 0:
                continue
            elif digit < 4:
                while digit:
                    temp_result.append(roman_digits[0])
                    digit -= 1
            elif digit == 4:
                temp_result.append(roman_digits[0] + roman_digits[1])
            elif 5 <= digit <= 8:
                temp_result.append(roman_digits[1])
                while digit > 5:
                    temp_result.append(roman_digits[0])
                    digit -= 1
            elif digit == 9:
                temp_result.append(roman_digits[0] + roman_digits[2])
            total_result.append(''.join(temp_result))
        return ''.join(reversed(total_result))
