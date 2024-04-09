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


# 227. Basic Calculator II  https://leetcode.com/problems/basic-calculator-ii/
# Given a string s which represents an expression, evaluate this expression and return its value.
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of
# [-2^31, 2^31 - 1].
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as
# eval().
# 1 <= s.length <= 3 * 10^5
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
# The answer is guaranteed to fit in a 32-bit integer.

SPACE = ' '
MULT = '*'
DIVISION = '/'
ADD = '+'
SUBST = '-'


class Solution:
    def calculate_stack(self, s: str) -> int:
        """ Time complexity: O(n). We iterate through string once and sum values in stack once.
            Space complexity: O(n). We use stack.
        """
        # empty string
        if not s:
            return 0

        stack = list()
        op = ADD
        curr_num = 0
        for i in range(len(s)):
            # if digit,  add to current number
            if s[i].isdigit():
                curr_num = curr_num * 10 + (ord(s[i]) - ord('0'))
            # if character is operation symbol or last symbol in the string
            if (not s[i].isdigit() and not s[i] == SPACE) or i == len(s) - 1:
                # previous operation symbol is '-'
                # push negative accumulated current number
                if op == SUBST:
                    stack.append(-curr_num)
                # previous operation symbol is '+'
                # push accumulated current number
                elif op == ADD:
                    stack.append(curr_num)
                # previous operation symbol is '*'
                # pop previous number, multiply by accumulated current number and push the result to stack
                elif op == MULT:
                    temp = stack.pop() * curr_num
                    stack.append(temp)
                # previous operation symbol is '/'
                # pop previous number, divide by accumulated current number and push the result to stack
                elif op == DIVISION:
                    temp = stack.pop()
                    if temp >= 0 or (temp % curr_num == 0):
                        temp //= curr_num
                    else:
                        temp = 1 + temp // curr_num
                    stack.append(temp)
                # update operation symbol
                op = s[i]
                # we handled operation symbol; next iteration we start accumulating new current number
                # (if it's not space)
                curr_num = 0
        return sum(stack)

    def calculate_no_stack(self, s: str) -> int:
        """ Time complexity: O(n). We iterate through string once.
            Space complexity: O(1).
        """
        # empty string
        if not s:
            return 0

        op = ADD
        curr_num = last_num = result = 0
        for i in range(len(s)):
            # if digit,  add to current number
            if s[i].isdigit():
                curr_num = curr_num * 10 + (ord(s[i]) - ord('0'))
            # if character is operation symbol or last symbol in the string
            if (not s[i].isdigit() and not s[i] == SPACE) or i == len(s) - 1:
                # previous operation symbol is '-'
                # add last (previous) number to result and set last number to negative accumulated current number
                if op == SUBST:
                    result += last_num
                    last_num = - curr_num
                # previous operation symbol is '+'
                # add last (previous) number to result and set last number to accumulated current number
                elif op == ADD:
                    result += last_num
                    last_num = curr_num
                # previous operation symbol is '*'
                # set last number to product of accumulated current number and last number
                elif op == MULT:
                    last_num *= curr_num
                # previous operation symbol is '/'
                # set last number to division of last number by accumulated current number
                elif op == DIVISION:
                    if last_num >= 0 or (last_num % curr_num == 0):
                        last_num //= curr_num
                    else:
                        last_num = 1 + last_num // curr_num
                # update operation symbol
                op = s[i]
                # we handled operation symbol; next iteration we start accumulating new current number
                # (if it's not space)
                curr_num = 0
        # when end of the string is reached, last number contains some value to be added to final result
        return result + last_num
