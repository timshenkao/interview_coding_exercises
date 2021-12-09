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


# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

CLOSING = {')': '(', '}': '{', ']': '['}


class Solution:
    def is_valid(self, s: str) -> bool:
        """ Time complexity: O(n). We iterate through the string once
            Space complexity: O(n). We use stack to keep brackets.
                              If brackets are of the same type, then O(1) as we don't need stack and just count
                              openings / closings.
        """
        # keep opening brackets in stack
        brackets_stack = list()
        for i in range(len(s)):
            # we see closing bracket
            if s[i] in CLOSING:
                # pop bracket from stack
                popped_bracket = brackets_stack.pop() if brackets_stack else ''
                # if popped bracket is not opening bracket for current symbol / bracket, then string is invalid
                if CLOSING[s[i]] != popped_bracket:
                    return False
            # we see opening bracket
            else:
                brackets_stack.append(s[i])
        # if there are unhandled brackets in stack, then string is invalid
        if brackets_stack:
            return False
        else:
            return True
