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

# 409. Longest Palindrome  https://leetcode.com/problems/longest-palindrome/
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that
# can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


class Solution:
    def longest_palindrome(self, s: str) -> int:
        """ Time complexity: O(n). We iterate through string once and through count table once.
            Space complexity: O(1). We create additional dict (count table) but it's maximum size is 26.
        """
        if not s:
            return 0

        if len(s) == 1:
            return 1

        count_table = dict()
        # count frequencies
        for ch in s:
            if ch in count_table:
                count_table[ch] += 1
            else:
                count_table[ch] = 1
        # check whether palindrome is possible and its length
        palindrome_max_length = 0
        one_char_flag = 0
        for ch, fr in count_table.items():
            if fr % 2 == 0:
                palindrome_max_length += fr
            else:  # fr % 2 == 1
                palindrome_max_length += fr - 1
                if not one_char_flag:
                    one_char_flag += 1
        palindrome_max_length += one_char_flag
        return palindrome_max_length
