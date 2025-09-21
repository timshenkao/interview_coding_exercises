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

# 8. String to Integer (atoi) https://leetcode.com/problems/string-to-integer-atoi/
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to
# C/C++'s atoi function).
# The algorithm for myAtoi(string s) is as follows:
#       Read in and ignore any leading whitespace.
#       Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if
#       it is either. This determines if the final result is negative or positive respectively. Assume the result is
#       positive if neither is present.
#       Read in next the characters until the next non-digit character or the end of the input is reached.
#       The rest of the string is ignored.
#       Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the
#       integer is 0. Change the sign as necessary (from step 2).
#       If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it
#       remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater
#       than 2^31 - 1 should be clamped to 2^31 - 1.
# Return the integer as the final result.
# Note:
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.


class Solution:
    def my_atoi(self, s: str) -> int:
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        # lstrip() creates a new string, but Python’s string slicing is considered O(1) extra space for fixed-size
        # operations (not storing the full string again)
        # s.length <= 200
        s = s.strip()
        if not s:
            return 0
        sign = -1 if s[0] == '-' else 1
        start = 0
        if s[0] in {'-', '+'}:
            start = 1

        num = 0
        for i in range(start, len(s)):
            if not s[i].isdigit():
                break
            num = num * 10 + ord(s[i]) - ord('0')
            if sign * num <= -2**31:
                return -2**31
            if sign * num >= 2**31 - 1:
                return 2**31 - 1
        return sign * num
