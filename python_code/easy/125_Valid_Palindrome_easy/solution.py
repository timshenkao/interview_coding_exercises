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


# 125. Valid Palindrome  https://leetcode.com/problems/valid-palindrome/
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
# numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.


class Solution:
    def is_palindrome(self, s: str) -> bool:
        """ Time complexity: O(n).
            Space complexity: O(1).
        """
        left = 0
        right = len(s) - 1

        # 2 pointers
        while left < right:
            # skip non-alphanumeric characters
            while left < right and not s[right].isalnum():
                right -= 1
            # skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            # if characters are the same, go on
            if left < right and s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            # case when left and right pointers point to the same element
            elif left == right and s[left].lower() == s[right].lower():
                return True
            # if characters are not the same
            else:
                return False
        return True

    def is_palindrome2(self, s):
        n = len(s)
        if n < 2:
            return True
        l = 0
        r = n - 1
        while l <= r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower() and s[l].isalnum() and s[r].isalnum():
                return False
            l += 1
            r -= 1
        return True
