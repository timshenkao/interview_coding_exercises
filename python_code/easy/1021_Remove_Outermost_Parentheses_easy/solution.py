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

# 1021. Remove Outermost Parentheses https://leetcode.com/problems/remove-outermost-parentheses/
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings,
# and + represents string concatenation.
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into
# s = A + B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk,
# where Pi are primitive valid parentheses strings.
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.


class Solution:
    def remove_outer_parentheses(self, s: str) -> str:
        """ Time complexity: O(n). We iterate through the whole string once.
            Space complexity: O(n). In the worst case scenario, we add all symbols to the final string.
        """
        depth = 0
        final_str = ""
        for elem in s:
            if elem == '(':
                # we see opening parentheses, i.e. one more nesting level
                depth += 1
                if depth > 1:
                    # we need to save opening parentheses from inner levels
                    final_str += elem
            elif elem == ')':
                # we see closing parentheses, i.e. we exit nesting level
                depth -= 1
                if depth > 0:
                    # for outermost parentheses, depth level is 0
                    final_str += elem
        return final_str
