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

# 224. Basic Calculator https://leetcode.com/problems/basic-calculator/
# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result
# of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such
# as eval().
# 1 <= s.length <= 3 * 10^5
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.


class Solution:
    def calculate(self, s):
        """ Time complexity: O(n) or O(n^2) ???.
            Space complexity: O(n).
        """
        def calc(n2, op, n1):
            return n1 + n2 if op == "+" else n1 - n2
        stack, i, num = [], 0, 0
        while i < len(s):
            j = i
            while j < len(s) and s[j].isdigit():
                num, j = num * 10 + int(s[j]), j + 1
            if i != j:
                stack.append(calc(num, stack.pop(), stack.pop()) if stack and s[i - 1] != "(" else num)
                num, j = 0, j - 1
            elif s[i] in "+-":
                stack.append(s[i])
            elif s[i] == ")" and len(stack) > 1:
                stack.append(calc(stack.pop(), stack.pop(), stack.pop()))
            i = j + 1
        return stack.pop()
