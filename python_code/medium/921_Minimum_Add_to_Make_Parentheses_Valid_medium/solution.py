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

from typing import List


#  921. Minimum Add to Make Parentheses Valid  https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# A parentheses string is valid if and only if:
#     It is the empty string,
#     It can be written as AB (A concatenated with B), where A and B are valid strings, or
#     It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
#     For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be
#     "())))".
# Return the minimum number of moves required to make s valid.
# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.

OPENING = '('
CLOSING = ')'


class Solution:
    def min_add_to_make_valid(self, s: str) -> int:
        """ Time complexity: O().
            Space complexity: O().
        """
        # empty string is a valid string
        if not s:
            return 0
        # no need for stack; just count unmatched parentheses
        unclosed_openings = unopened_closings = 0
        for ch in s:
            if ch == OPENING:
                unclosed_openings += 1
            elif ch == CLOSING:
                # if there are unmatched opening parentheses, decrease count
                if unclosed_openings:
                    unclosed_openings -= 1
                # if there is no unmatched opening parentheses, then this closing parentheses is unmatched
                else:
                    unopened_closings += 1
        return unclosed_openings + unopened_closings
