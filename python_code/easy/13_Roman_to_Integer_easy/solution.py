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

# 13. Roman to Integer  https://leetcode.com/problems/roman-to-integer/
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
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#    I can be placed before V (5) and X (10) to make 4 and 9.
#    X can be placed before L (50) and C (100) to make 40 and 90.
#    C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


class Solution:
    def roman_to_integer_brute(self, s: str) -> int:
        """ Time complexity: O(n). We iterate through the whole string once.
            Space complexity: O(1). We just use 2 variables: number and roman_length
        """
        number = 0
        roman_length = len(s) - 1

        # we iterate from right to left
        while roman_length > -1:
            if s[roman_length] == "I":
                number += 1 
                roman_length -= 1
            elif s[roman_length] == "V":
                # V can be preceded by I. In this case, it's 4 and we have to skip I
                if roman_length > 0 and s[roman_length - 1] == "I":
                    number += 4 
                    roman_length -= 2
                # V is 5 in this case
                else:
                    number += 5 
                    roman_length -= 1
            # X can be preceded by I. In this case, it's 9 and we have to skip I
            elif s[roman_length] == "X":
                if roman_length > 0 and s[roman_length - 1] == "I":
                    number += 9 
                    roman_length -= 2
                # X is 10 in this case
                else:
                    number += 10 
                    roman_length -= 1
            # L can be preceded by X. In this case, it's 40 and we have to skip X
            elif s[roman_length] == "L":
                if roman_length > 0 and s[roman_length - 1] == "X":
                    number += 40 
                    roman_length -= 2
                # L is 50 in this case
                else:
                    number += 50 
                    roman_length -= 1
            # C can be preceded by X. In this case, it's 90 and we have to skip X
            elif s[roman_length] == "C":
                if roman_length > 0 and s[roman_length - 1] == "X":
                    number += 90 
                    roman_length -= 2
                # C is 100 in this case
                else:
                    number += 100 
                    roman_length -= 1
            # D can be preceded by C. In this case, it's 400 and we have to skip C
            elif s[roman_length] == "D":
                if roman_length > 0 and s[roman_length - 1] == "C":
                    number += 400 
                    roman_length -= 2
                # D is 500 in this case
                else:
                    number += 500 
                    roman_length -= 1
            # M can be preceded by C. In this case, it's 900 and we have to skip C
            elif s[roman_length] == "M":
                if roman_length > 0 and s[roman_length - 1] == "C":
                    number += 900 
                    roman_length -= 2
                # D is 500 in this case
                else:
                    number += 1000 
                    roman_length -= 1
        return number

    def roman_to_integer_optimal(self, s: str) -> int:
        """ Time complexity: O(n). We iterate through the whole string once.
            Space complexity: O(1).
        """
        correspondence = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # initialize number with right-most digit
        number = correspondence.get(s[-1])
        # we iterate from right to left
        for i in reversed(range(len(s) - 1)):
            # if the current roman integer is less than the next one, subtract the current roman integer
            if correspondence[s[i]] < correspondence[s[i + 1]]:
                number -= correspondence[s[i]]
            # just add the current roman integer
            else:
                number += correspondence[s[i]]
        return number
