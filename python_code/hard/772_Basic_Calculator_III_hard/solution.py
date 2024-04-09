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

# 772. Basic Calculator III https://leetcode.com/problems/basic-calculator-iii/
# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open
# '(' and closing parentheses ')'. The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of
# [-2^31, 2^31 - 1].
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as
# eval().
# 1 <= s <= 10^4
# s consists of digits, '+', '-', '*', '/', '(', and ')'.
# s is a valid expression.


class Solution:
    def calculate(self, s: str) -> int:
        """ Time complexity: O(n).
            Space complexity: O(n).
        """
        def calc():
            b = nums.pop()
            a = nums.pop()
            op = ops.pop()
            if op == '+':
                nums.append(a + b)
            elif op == '-':
                nums.append(a - b)
            elif op == '*':
                nums.append(a * b)
            else:  # op == '/'
                nums.append(int(a / b))

        def precedes(prev: str, curr: str) -> bool:
            """
            Returns True if the previous character is a operator and the priority of
            the previous operator >= the priority of the current character (operator).
            """
            if prev == '(':
                return False
            return prev in '*/' or curr in '+-'

        nums = []
        ops = []
        i = 0
        has_prev_num = False

        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = ord(c) - ord('0')
                while i + 1 < len(s) and s[i + 1].isdigit():
                    num = num * 10 + (ord(s[i + 1]) - ord('0'))
                    i += 1
                nums.append(num)
                has_prev_num = True
            elif c == '(':
                ops.append('(')
                has_prev_num = False
            elif c == ')':
                while ops[-1] != '(':
                    calc()
                ops.pop()  # Pop '('
            elif c in '+-*/':
                if not has_prev_num:  # Handle input like "-1-(-1)"
                    num.append(0)
                while ops and precedes(ops[-1], c):
                    calc()
                ops.append(c)
            i += 1

        while ops:
            calc()

        return nums.pop()
