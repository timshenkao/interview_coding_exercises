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
# 1 <= s.length <= 2 * 105
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
