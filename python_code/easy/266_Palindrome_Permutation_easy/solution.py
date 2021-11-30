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

# 266. Palindrome Permutation https://leetcode.com/problems/palindrome-permutation/
# Given a string s, return true if a permutation of the string could form a palindrome.


class Solution:
    def can_permute_palindrome(self, s: str) -> bool:
        """ Time complexity: O(n). We iterate through string once and through count table once.
            Space complexity: O(1).
        """
        if not s:
            return False

        if len(s) == 1:
            return True

        count_table = dict()
        # count frequencies
        for ch in s:
            if ch in count_table:
                count_table[ch] += 1
            else:
                count_table[ch] = 1
        # check whether palindrome is possible and its length
        one_char_flag = 0
        for ch, fr in count_table.items():
            if fr % 2 == 1:
                if not one_char_flag:
                    one_char_flag = 1
                else:
                    return  False
        return True
