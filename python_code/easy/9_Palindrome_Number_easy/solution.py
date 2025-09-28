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

# 9. Palindrome Number  https://leetcode.com/problems/palindrome-number/
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.
# Could you solve it without converting the integer to a string?

class Solution:
    def is_palindrome_string(self, x: int) -> bool:
        """ Time complexity: O(log x).
            Space complexity: O(log x). String representation of x requires log x.
            Actually this is the fastest approach because of built-in string conversion and string comparison. No
            divisions or other math operations
        """
        # convert to string
        # it requires O(log x) time and space
        x_str = str(x)
        left = 0
        right = len(x_str) - 1
        # iterate from both ends; TC O(log x)
        while left <= right:
            if x_str[left] != x_str[right]:
                return False
            left += 1
            right -= 1
        return True

    def is_palindrome_digit(self, x: int) -> bool:
        """ Time complexity: O(log x).
            Space complexity: O(log x). There are (log x) digits in x.
        """
        # handle edge cases
        if x < 0:
            return False
        if x == 0:
            return True

        # keep list of digits, O(log x)
        x_digits = list()
        while x:
            x, digit = divmod(x, 10)
            x_digits.append(digit)

        left = 0
        right = len(x_digits) - 1
        # iterate from both ends and compare digits
        while left <= right:
            if x_digits[left] != x_digits[right]:
                return False
            left += 1
            right -= 1
        return True

    def is_palindrome_reverted_number(self, x: int) -> bool:
        """ Time complexity: O(log x).
            Space complexity: O(1).
        """
        # handle edge cases
        if x < 0:
            return False
        if x == 0:
            return True
        # revert the second part of the number and compare it with the first half of the number
        # how do we know that we've reached the half of the number?
        # As we divide the number by 10, and multiplied the reversed number by 10,
        # when the original number is less than the reversed number, we processed half of the number digits.
        reverted_number = 0
        base = 10
        # when number ends with 0, there is leading zero
        if x % base == 0:
            return False
        while x > reverted_number:
            reverted_number = reverted_number * base + x % base
            x //= base

        # When number of digits is even
        if x == reverted_number:
            return True
        # When number of digits is odd, we can get rid of the middle digit
        elif x == reverted_number // base:
            return True
        else:
            return False
