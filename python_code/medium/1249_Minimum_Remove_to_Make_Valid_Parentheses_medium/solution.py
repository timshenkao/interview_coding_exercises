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


#  1249. Minimum Remove to Make Valid Parentheses
#  https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
# parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
#     It is the empty string, contains only lowercase characters, or
#     It can be written as AB (A concatenated with B), where A and B are valid strings, or
#     It can be written as (A), where A is a valid string.
# 1 <= s.length <= 105
# s[i] is either'(' , ')', or lowercase English letter.


OPENING = '('
CLOSING = ')'


class Solution:
    def min_remove_to_make_valid(self, s: str) -> str:
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        # empty string is a valid string
        if not s:
            return ""

        # no need for stack; keep indices of parentheses to remove
        unclosed_openings = list()
        unopened_closings = list()
        for i in range(len(s)):
            if s[i] == OPENING:
                unclosed_openings.append(i)
            elif s[i] == CLOSING:
                # if there is unmatched opening parentheses, pop it
                if unclosed_openings:
                    unclosed_openings.pop()
                    # if there is no unmatched opening parentheses, then this closing parentheses is unmatched
                else:
                    unopened_closings.append(i)
        unclosed_openings = set(unclosed_openings)
        unopened_closings = set(unopened_closings)

        result = list()
        # construct output string via list
        for i in range(len(s)):
            if (i not in unclosed_openings) and (i not in unopened_closings):
                result.append(s[i])

        return "".join(result)
