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

# 1541. Minimum Insertions to Balance a Parentheses String
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/
# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
#       Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
#       Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.
# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.
# Return the minimum number of insertions needed to make s balanced.
# 1 <= s.length <= 10^5
# s consists of '(' and ')' only.


class Solution:
    def min_insertions(self, s: str) -> int:
        """ Time complexity: O(n).
            Space complexity: O(1)
        """
        needed_right = 0   # Increment by 2 for each '('.
        missing_left = 0   # Increment by 1 for each missing '('.
        missing_right = 0  # Increment by 1 for each missing ')'.

        for c in s:
            if c == '(':
                if needed_right % 2 == 1:
                    # e.g. '()(...'
                    missing_right += 1
                    needed_right -= 1
                needed_right += 2
            else:  # c == ')'
                needed_right -= 1
                if needed_right < 0:
                    # e.g. '()))...'
                    missing_left += 1
                    needed_right += 2
        return needed_right + missing_left + missing_right
